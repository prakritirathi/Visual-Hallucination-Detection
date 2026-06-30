def extract_objects(doc):
    """
    Extract all noun chunks (objects) from the caption.
    Returns a list of unique object names.
    """

    objects = []

    for chunk in doc.noun_chunks:
        obj = chunk.text.lower().strip()

        if obj not in objects:
            objects.append(obj)

    return objects