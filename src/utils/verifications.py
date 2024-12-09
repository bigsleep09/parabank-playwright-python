from playwright.sync_api import expect


class Verifications:

    def expected_element_is_visible(self, selector: str):
        expect(selector).to_be_visible()

    def expected_element_is_enabled(self, selector: str):
        expect(selector).to_be_enabled()
