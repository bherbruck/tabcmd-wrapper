# tabcmd-wrapper

[license-image]: https://img.shields.io/npm/l/make-coverage-badge.svg
[license-url]: https://opensource.org/licenses/MIT

[![License][license-image]][license-url]

Tabcmd wrapper for Python

## Installation

```text
$ pip install git+https://github.com/bherbruck/tabcmd-wrapper
```

## Usage

```python
import tabcmd

sess = tabcmd.Session()

sess.login('tabcmd_site',
           'tableau_username',
           'tableau_password')

sess.export(view_path='workbook/view',
            file_path='./view.png',
            export_format=tabcmd.ExportFormat.PNG,
            width=1920, height=1080)

# some other commands...

sess.logout()

```
