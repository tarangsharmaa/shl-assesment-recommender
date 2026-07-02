from langchain_core.documents import Document


class DocumentBuilder:

    def build_documents(self, catalog):

        documents = []

        for assessment in catalog:

            text = f"""
Name: {assessment.get('name', '')}
Description: {assessment.get('description', '')}
Job Levels: {", ".join(assessment.get('job_levels', []))}
Duration: {assessment.get('duration', '')}
Category: {", ".join(assessment.get('keys', []))}
"""

            document = Document(
                page_content=text,
                metadata={
                    "name": assessment.get("name"),
                    "link": assessment.get("link"),
                    "duration": assessment.get("duration"),
                    "job_levels": assessment.get("job_levels"),
                    "keys": assessment.get("keys")
                }
            )

            documents.append(document)

        return documents