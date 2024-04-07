from seleniumbase import SB

def verify_success(sb):
    sb.assert_exact_text("我的E政府", "h1", timeout = 8)
    sb.sleep(4)

with SB(uc_cdp=True, guest_mode=True) as sb:
    sb.open("https://www.gov.tw/")
    try:
        verify_success(sb)
    except Exception:
        sb.sleep(4)
        if sb.assert_exact_text("www.gov.tw", "h1"):
            # 待確認
            sb.click('input[value*="Verify"]')
        try:
            verify_success(sb)
        except Exception:
            raise Exception("Detected!")