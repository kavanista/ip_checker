from unittest import TestCase
import utils 

class TestSniffer(TestCase):

    def test_server_is_iis(self):
        server = "Microsoft-IIS/7.0"
        self.assertTrue(utils.check_server_type_version(server, "iis", "7.0"))

        server = "Apache"
        self.assertFalse(utils.check_server_type_version(server, "iis", "7.0"))
        
    def test_server_is_nginx_12(self):
        server = "Nginx/1.2.0"
        self.assertTrue(utils.check_server_type_version(server, "nginx", 1.2))
        
        server = "Apache"
        self.assertFalse(utils.check_server_type_version(server, "nginx", 1.2))


    def test_index_has_dir_listing(self):
        s = open("index-test.txt").read()
        self.assertTrue("Y", utils.index_has_dir_listing(s))

        s = "Testy McTestface"
        self.assertEquals("N", utils.index_has_dir_listing(s))
