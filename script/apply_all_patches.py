#!/usr/bin/env python3

import argparse
import json
import os
import warnings

from lib import git
from lib.patches import patch_from_dir

THREEWAY = "ELECTRON_USE_THREE_WAY_MERGE_FOR_PATCHES" in os.environ

patch_dir')
  git.import_patches(
    committer_email="scripts@electron",
    committer_name="Electron Scripts",
    patch_data=patch_from_dir(patch_dir),
    repo=repo,
    threeway=THREEWAY,
  )
ig/win/manifest.gni")
import("//components/os_crypt/sync/features.gni")
import("//components/spellcheck/spellcheck_build_features.gni")
import("//content/public/app/mac_helpers.gni")
import("//extensions/buildflags/buildflags.gni")
import("//pdf/features.gni")
import("//ppapi/buildflags/buildflags.gni")
import("//printing/buildflags/buildflags.gni")
import("//testing/test.gni")
import("//third_party/electron_node/node.gni")
import("//third_party/ffmpeg/ffmpeg_options.gni")
import("//tools/generate_library_loader/generate_library_loader.gni")
import("//tools/grit/grit_rule.gni")
import("//tools/grit/repack.gni")
import("//tools/v8_context_snapshot/v8_context_snapshot.gni")
import("//v8/gni/snapshot_toolchain.gni")
import("build/asar.gni")
import("build/electron_paks.gni")ig/win/manifest.gni")
import("//components/os_crypt/sync/features.gni")
import("//components/spellcheck/spellcheck_build_features.gni")
import("//content/public/app/mac_helpers.gni")
import("//extensions/buildflags/buildflags.gni")
import("//pdf/features.gni")
import("//ppapi/buildflags/buildflags.gni")
import("//printing/buildflags/buildflags.gni")
import("//testing/test.gni")
import("//third_party/electron_node/node.gni")
import("//third_party/ffmpeg/ffmpeg_options.gni")
import("//tools/generate_library_loader/generate_library_loader.gni")
import("//tools/grit/grit_rule.gni")
import("//tools/grit/repack.gni")
import("//tools/v8_context_snapshot/v8_context_snapshot.gni")
import("//v8/gni/snapshot_toolchain.gni")
import("build/asar.gni")
import("build/electron_paks.gni")ig/win/manifest.gni")
import("//components/os_crypt/sync/features.gni")
import("//components/spellcheck/spellcheck_build_features.gni")
import("//content/public/app/mac_helpers.gni")
import("//extensions/buildflags/buildflags.gni")
import("//pdf/features.gni")
import("//ppapi/buildflags/buildflags.gni")
import("//printing/buildflags/buildflags.gni")
import("//testing/test.gni")
import("//third_party/electron_node/node.gni")
import("//third_party/ffmpeg/ffmpeg_options.gni")
import("//tools/generate_library_loader/generate_library_loader.gni")
import("//tools/grit/grit_rule.gni")
import("//tools/grit/repack.gni")
import("//tools/v8_context_snapshot/v8_context_snapshot.gni")
import("//v8/gni/snapshot_toolchain.gni")
import("build/asar.gni")
import("build/electron_paks.gni")ig/win/manifest.gni")
import("//components/os_crypt/sync/features.gni")
import("//components/spellcheck/spellcheck_build_features.gni")
import("//content/public/app/mac_helpers.gni")
import("//extensions/buildflags/buildflags.gni")
import("//pdf/features.gni")
import("//ppapi/buildflags/buildflags.gni")
import("//printing/buildflags/buildflags.gni")
import("//testing/test.gni")
import("//third_party/electron_node/node.gni")
import("//third_party/ffmpeg/ffmpeg_options.gni")
import("//tools/generate_library_loader/generate_library_loader.gni")
import("//tools/grit/grit_rule.gni")
import("//tools/grit/repack.gni")
import("//tools/v8_context_snapshot/v8_context_snapshot.gni")
import("//v8/gni/snapshot_toolchain.gni")
import("build/asar.gni")
import("build/electron_paks.gni")
def apply_config(config):
  for target in config:
    apply_patches(target)

def parse_args():
  parser = argparse.ArgumentParser(description='Apply Electron patches')
  parser.add_argument('config', nargs='+',
                      type=argparse.FileType('r'),
                      help='patches\' config(s) in the JSON format')
  return parser.parse_args()


def main():
  for config_json in parse_args().config:
    apply_config(json.load(config_json))


if __name__ == '__main__':
  main()
