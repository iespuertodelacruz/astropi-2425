[no-cd]
@run:
    uv run main.py

zip:
    rm -f astropi-matraka.zip && zip astropi-matraka.zip src/*.py
