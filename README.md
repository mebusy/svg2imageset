# svg2imageset

python3 script to convert SVG to iOS .imageset

## Requirement

1. python3.6+
2. [CairoSVG](https://cairosvg.org/documentation/)
    ```bash
    pip3 install cairosvg --user
    ```

## Usage

```bash
usage: python3 svg2imageset.py <path-2-svg> <icon-width> [outpath]

@ icon-width: specify the output width of the @1x png image
@ outpath:  `.` by default
```

Example:

```bash
python3 ./svg2imageset.py test_arrow_circle_down.svg  60 
```

I will generate such files...

```bash
test_arrow_circle_down.imageset
├── Contents.json
├── test_arrow_circle_down.png
├── test_arrow_circle_down_2x.png
└── test_arrow_circle_down_3x.png
```



