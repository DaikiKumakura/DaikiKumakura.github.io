from pathlib import Path
import shutil
import subprocess
import unittest
from jinja2 import Environment, FileSystemLoader, StrictUndefined

BASE=Path(__file__).resolve().parent


class AnalyticsTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('node'), 'Node runtime unavailable')
    def test_consent_runtime(self):
        subprocess.run(['node', str(BASE/'test_analytics.cjs')],check=True,capture_output=True,text=True)

    def test_preview_never_includes_tracking_or_consent_controls(self):
        env=Environment(loader=FileSystemLoader(BASE/'templates'),undefined=StrictUndefined)
        env.globals['about_page']=None
        site=dict(name='Example',analytics_measurement_id='G-TEST123',github='#',qiita='#',docker='#',linkedin='#',orcid='#',scholar='#')
        context=dict(site=site,lang='en',description='Example',title='Example',root='',alternatives={},math=False,ui=dict(skip='Skip',navigation='Navigation',preview='Preview',nav={}),active='')
        live=env.get_template('base.html').render(**context,preview=False)
        preview=env.get_template('base.html').render(**context,preview=True)
        self.assertIn('data-measurement-id="G-TEST123"',live)
        self.assertIn('id="analytics-notice"',live)
        self.assertNotIn('assets/analytics.js',preview)
        self.assertNotIn('id="analytics-notice"',preview)


if __name__=='__main__':unittest.main()
