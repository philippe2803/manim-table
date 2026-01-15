import subprocess
import pytest
import os
import shutil

# List of scenes to test
SCENES = [
    "TableDemo",
    "TableWithExplicitHeader",
    "BorderlessTable",
    "TableColorScene",
    "TableColorResizePreservationScene",
    "TableScaledResizeScene",
    "TableColumnOperationsScene",
]

@pytest.fixture(scope="module")
def cleanup_videos():
    """Fixture to cleanup the videos directory after tests."""
    yield
    # Cleanup code (optional, decided to keep videos for inspection or ignore them via gitignore)
    # if os.path.exists("videos"):
    #     shutil.rmtree("videos")

@pytest.mark.parametrize("scene_name", SCENES)
def test_scene_rendering(scene_name):
    """
    Test that the scene renders successfully (exit code 0).
    We use the -w flag to write to file, avoiding opening a window.
    """
    # Construct the command: manimgl tests/scenes_tests.py <SceneName> -w
    command = [
        "manimgl",
        "tests/scenes_tests.py",
        scene_name,
        "-w",  # Write to file
    ]
    
    # Run the command
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    
    # Check if the command failed
    if result.returncode != 0:
        pytest.fail(f"Scene {scene_name} failed with error:\n{result.stderr}")
