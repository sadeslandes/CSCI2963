'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual( 
                run_markdown('this line has no special handling'), 
                '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual( 
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')
    
    def test_headers(self):
        self.assertEqual(
                run_markdown('#h1 header'),'<h1>h1 header</h1>')
        self.assertEqual(
                run_markdown('##h2 header'),'<h2>h2 header</h2>')
        self.assertEqual(
                run_markdown('###h3 header'),'<h3>h3 header</h3>')
    
    def test_blockquote(self):
        self.assertEqual(
                run_markdown('>single line'),'<blockquote><p>single line</p></blockquote>')
        self.assertEqual(
                run_markdown('>blockquote\nNo blockquote\n>#header blockquote'),'<blockquote><p>blockquote</p></blockquote>\r\n<p>No blockquote</p>\r\n<blockquote><h1>header blockquote</h1></blockquote>')
        self.assertEqual(
                run_markdown('>multiline\n>blockquote'),'<blockquote><p>multiline</p>\r\n<p>blockquote</p></blockquote>')
        self.assertEqual(
                run_markdown('>multiline\n>blockquote\nWith a no blockquote line at the end'),'<blockquote><p>multiline</p>\r\n<p>blockquote</p></blockquote>\r\n<p>With a no blockquote line at the end</p>')        
        
    
if __name__ == '__main__':
    unittest.main()
