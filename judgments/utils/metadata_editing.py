from caselawclient.models.documents import Document
from caselawclient.models.documents.metadata.fields.field import MetadataField, MetadataStringValue
from caselawclient.models.documents.metadata.fields.source import MetadataSource


def add_editor_title_claim_if_changed(document: Document, submitted_title: str) -> bool:
    current_title = document.metadata.title.value
    if current_title == submitted_title:
        return False

    document.metadata_fields.add(
        MetadataField(
            name="title",
            value=MetadataStringValue(submitted_title),
            source=MetadataSource.EDITOR,
        ),
    )
    return True


def save_title_from_preview_form(document: Document, form_value: str) -> None:
    if add_editor_title_claim_if_changed(document, form_value):
        document.save_metadata_fields()
