from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(summary, selected_questions):

    pdf_file = "AI_Report.pdf"
    doc = SimpleDocTemplate(pdf_file)
    styles = getSampleStyleSheet()

    story = []

    # Title
    story.append(Paragraph("<b>AI DATA ANALYST REPORT</b>", styles["Title"]))

    # Summary
    story.append(Paragraph("<br/><b>Dataset Summary</b>", styles["Heading2"]))

    story.append(Paragraph(f"Total Rows : {summary['Total Rows']}", styles["BodyText"]))
    story.append(Paragraph(f"Total Columns : {summary['Total Columns']}", styles["BodyText"]))
    story.append(Paragraph(f"Missing Values : {summary['Missing Values']}", styles["BodyText"]))
    story.append(Paragraph(f"Duplicate Rows : {summary['Duplicate Rows']}", styles["BodyText"]))

    # AI Section
    story.append(Paragraph("<br/><b>Selected AI Questions</b>", styles["Heading1"]))

    # IMPORTANT: loop must be INSIDE function
    for chat in selected_questions:

        story.append(
            Paragraph(
                f"<b>Question:</b> {chat['question']}",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Answer:</b> {chat['answer']}",
                styles["BodyText"]
            )
        )

    doc.build(story)

    return pdf_file