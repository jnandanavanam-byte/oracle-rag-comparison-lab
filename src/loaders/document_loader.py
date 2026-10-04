"""
Document Loader

Supports:
- PDF
- DOCX
- XLSX
"""

from pathlib import Path


class DocumentLoader:

    def __init__(self, docs_path: str):
        self.docs_path = docs_path

    def load(self):
        """
        Load documents from docs folder.

        Returns
        -------
        list
            Collection of LangChain documents.
        """
        documents = []

        # Implementation will be added
        return documents