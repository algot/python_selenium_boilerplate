class TestSample:
    def test_sample(self, browser, env_config):
        browser.get(env_config.url)
