{
  description = "Hackergame 2024";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          name = "hackergame";
          packages = with pkgs; [
            nodejs
            yarn
            python3
            python3Packages.flask
            python3Packages.numpy
            python3Packages.pwntools
            python3Packages.pycryptodome
            python3Packages.autopep8
          ];

          shellHook = ''
            export __ETC_PROFILE_NIX_SOURCED=1
            exec $SHELL
          '';
        };
      }
    );
}
