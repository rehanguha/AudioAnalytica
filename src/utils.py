from pathlib import Path

def extractFilename(PATH):
    return str(Path(PATH).stem)