from .text import parse_opml


def test_parse_opml():
    """Test for OPML parser"""
    found = sorted(parse_opml("samples/test.opml"))
    assert found[0] == (
        "a-phone-call-from-paul",
        "http://feeds.soundcloud.com/users/soundcloud:users:148802660/sounds.rss",
    )
    assert found[1] == (
        "the-skeptics-guide-to-the-universe",
        "http://www.theskepticsguide.org/feed/rss.aspx?feed=sgu",
    )
