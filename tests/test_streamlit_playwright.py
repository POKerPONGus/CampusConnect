from playwright.sync_api import sync_playwright, expect


APP_URL = "http://localhost:8501"


def test_valid_student_can_enroll():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(APP_URL)

        page.get_by_role("textbox", name="Enter Student ID", exact=True).fill("student_1")
        page.get_by_role("button", name="Enroll").click()

        expect(page.get_by_text("Student enrolled successfully")).to_be_visible()
        expect(page.get_by_text("student_1")).to_be_visible()

        browser.close()


def test_duplicate_student_shows_warning():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(APP_URL)

        enroll_box = page.get_by_role("textbox", name="Enter Student ID", exact=True)

        enroll_box.fill("student_1")
        page.get_by_role("button", name="Enroll").click()

        enroll_box.fill("student_1")
        page.get_by_role("button", name="Enroll").click()

        expect(page.get_by_text("Already enrolled")).to_be_visible()

        browser.close()


def test_invalid_empty_student_id_shows_error():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(APP_URL)

        page.get_by_role("textbox", name="Enter Student ID", exact=True).fill("")
        page.get_by_role("button", name="Enroll").click()

        expect(page.get_by_text("Invalid student ID")).to_be_visible()

        browser.close()


def test_course_full_shows_warning():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(APP_URL)

        enroll_box = page.get_by_role(
            "textbox",
            name="Enter Student ID",
            exact=True
        )

        # Fill course capacity
        enroll_box.fill("student_1")
        page.get_by_role("button", name="Enroll").click()

        enroll_box.fill("student_2")
        page.get_by_role("button", name="Enroll").click()

        enroll_box.fill("student_3")
        page.get_by_role("button", name="Enroll").click()

        # Attempt extra enrollment
        enroll_box.fill("student_4")
        page.get_by_role("button", name="Enroll").click()

        expect(page.get_by_text("Course full")).to_be_visible()

        browser.close()


def test_drop_existing_student():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(APP_URL)

        # Enroll first
        page.get_by_role(
            "textbox",
            name="Enter Student ID",
            exact=True
        ).fill("student_1")

        page.get_by_role("button", name="Enroll").click()

        expect(
            page.get_by_text("Student enrolled successfully")
        ).to_be_visible()

        # Re-locate drop textbox after Streamlit reruns
        page.get_by_role(
            "textbox",
            name="Enter Student ID to Drop",
            exact=True
        ).fill("student_1")

        page.get_by_role("button", name="Drop").click()

        expect(
            page.get_by_text("Student dropped successfully")
        ).to_be_visible()

        browser.close()

def test_drop_non_enrolled_student():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(APP_URL)

        drop_box = page.get_by_role(
            "textbox",
            name="Enter Student ID to Drop",
            exact=True
        )

        drop_box.fill("student_999")
        page.get_by_role("button", name="Drop").click()

        expect(
            page.get_by_text("Student not enrolled")
        ).to_be_visible()

        browser.close()