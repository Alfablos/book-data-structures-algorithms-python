{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixpkgs-unstable";
  };
  outputs = { self, nixpkgs, ... }:
  let
    forAllSystems = f: nixpkgs.lib.genAttrs [ "x86_64-linux" "aarch64-linux" ] ( system:
      f (import nixpkgs { inherit system; })
    );
    mkLibraryPath = pkgs: with pkgs; lib.makeLibraryPath [ ];

    pythonForPkgs = pkgs: pkgs.python313;
  in
  {
    devShells = forAllSystems (pkgs:
      {
        default = with pkgs;
        let
          python = pythonForPkgs pkgs;
          pythonPackages = python.pkgs;
        in
      pkgs.mkShell {
        packages = [
          (writeShellScriptBin "pycharm" "${tmux}/bin/tmux new -d 'pycharm-professional .'")
          python
          uv
          pythonPackages.ruff
        ];

          # export "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${mkLibraryPath pkgs}"
        shellHook = ''
          export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${mkLibraryPath pkgs}"
          export UV_PYTHON_DOWNLOADS=never
          
          exec -l zsh
        '';
      };
    });
  };
}






