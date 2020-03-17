import subprocess


class ExportFormat:
    CSV = '--csv'
    PDF = '--pdf'
    PNG = '--png'
    FULL_PDF = '--fullpdf'


class PageLayout:
    LANDSCAPE = 'landscape'
    PORTRAIT = 'portrait'


class PageSize:
    UNSPECIFIED = 'unspecified'
    LETTER = 'letter'
    LEGAL = 'legal'
    NOTE_FOLIO = 'note folio'
    TABLOID = 'tabloid'
    LEDGER = 'ledger'
    STATEMENT = 'statement'
    EXECUTIVE = 'executive'
    A3 = 'a3'
    A4 = 'a4'
    A5 = 'a5'
    B4 = 'b4'
    B5 = 'b5'
    QUARTO = 'quarto'


class Session:
    def __init__(self, tabcmd_path='tabcmd', certcheck=False):
        """Initialize a tabcmd session, not yet logged in.

        Args:
            tabcmd_path (str, optional):
                Path to tabcmd executable. Defaults to 'tabcmd'.
            certcheck (bool, optional):
                False to add '--no-certcheck' to all executions.
                Defaults to False.
        """
        self.tabcmd_path = tabcmd_path
        self.certcheck = certcheck
        self.is_logged_in = False

    def execute(self, command):
        if command[0] != self.tabcmd_path:
            command.insert(0, self.tabcmd_path)
        if not self.certcheck:
            command.append('--no-certcheck')
        command = [str(i) for i in command]
        return subprocess.call(command)

    def login(self, site, username, password):
        """Log in to the tabcmd session.

        Args:
            site (str): Tableau site url
            username (str): Tableau username
            password (str): Tableau password
        """
        command = [
            self.tabcmd_path,
            'login',
            '-s', site,
            '-u', username,
            '-p', password
        ]
        self.is_logged_in = True if self.execute(command) == 0 else False

    def logout(self):
        """Log out of the tabcmd session.
        """
        command = [
            self.tabcmd_path,
            'logout'
        ]
        self.is_logged_in = False if self.execute(command) == 0 else True

    def refresh_data_source(self, data_source):
        """Refresh a data source.

        Args:
            data_source (str): Path to the data source
        """
        command = [
            self.tabcmd_path,
            'refreshextracts',
            '--datasource', data_source
        ]
        self.execute(command)

    def export(self, view_path, file_path, export_format=ExportFormat.CSV,
               page_layout='landscape', page_size='letter',
               width=800, height=600):
        """Export a view to a local path.

        Args:
            view_path (str): Path to the Tableau view
            file_path (str): Path to save the export to
            export_format (str, optional):
                Format of the export.Defaults to ExportFormat.CSV
            page_layout (str, optional): Page layout. Defaults to 'landscape'.
            page_size (str, optional): Page size. Defaults to 'letter'.
            width (int, optional): Width. Defaults to 800.
            height (int, optional): Height. Defaults to 600.
        """
        command = [
            self.tabcmd_path,
            'export',
            view_path,
            '--filename', file_path,
            export_format,
            '--pagelayout', page_layout,
            '--pagesize', page_size,
            '--width', width,
            '--height', height
        ]
        self.execute(command)

    def run_schedule(self):
        """TODO
        """
        pass
