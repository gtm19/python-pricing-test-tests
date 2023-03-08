def pytest_emoji_passed(config):
    return "✅", "PASSED ✅ "


def pytest_emoji_failed(config):
    return "🚨", "FAILED 🚨 "
