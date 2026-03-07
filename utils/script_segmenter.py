def segment_script(text):

    length = len(text)

    hook = text[:200]
    intro = text[200:600]
    body = text[600:length-200]
    outro = text[length-200:]

    return {
        "hook": hook,
        "intro": intro,
        "body": body,
        "outro": outro
    }