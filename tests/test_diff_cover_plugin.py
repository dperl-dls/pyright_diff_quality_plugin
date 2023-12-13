from diff_cover.diff_quality_tool import main


def test_plugin_can_load():
    main(["diff-quality","--violations","pyright"])

def test_run_on_hyperion():
    import os
    os.chdir("../hyperion/hyperion/")
    main(["diff-quality","--violations","pyright"])
