from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from app.utils.config import AZURE_AI_SERVICE_ENDPOINT, AZURE_AI_SERVICE_KEY

# sample document
formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

document_analysis_client = DocumentAnalysisClient(
    endpoint=AZURE_AI_SERVICE_ENDPOINT,
    credential=AzureKeyCredential(AZURE_AI_SERVICE_KEY),
)

poller = document_analysis_client.begin_analyze_document_from_url(
    "prebuilt-layout", formUrl
)
result = poller.result()

for idx, style in enumerate(result.styles):
    print(
        "Document contains {} content".format(
            "handwritten" if style.is_handwritten else "no handwritten"
        )
    )

for page in result.pages:
    for line_idx, line in enumerate(page.lines):
        print(
            "...Line # {} has text content '{}'".format(
                line_idx, line.content.encode("utf-8")
            )
        )

    for selection_mark in page.selection_marks:
        print(
            "...Selection mark is '{}' and has a confidence of {}".format(
                selection_mark.state, selection_mark.confidence
            )
        )

for table_idx, table in enumerate(result.tables):
    print(
        "Table # {} has {} rows and {} columns".format(
            table_idx, table.row_count, table.column_count
        )
    )

    for cell in table.cells:
        print(
            "...Cell[{}][{}] has content '{}'".format(
                cell.row_index,
                cell.column_index,
                cell.content.encode("utf-8"),
            )
        )

print("----------------------------------------")
