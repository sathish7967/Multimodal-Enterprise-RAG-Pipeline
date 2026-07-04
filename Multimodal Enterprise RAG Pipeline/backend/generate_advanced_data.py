import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def build_multipage_dataset(filename="enterprise_analytics_report.pdf"):
    # Set document properties with multi-page flow configurations
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom structural UI typography styles
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=16, leading=20, textColor=colors.HexColor('#1E3A8A'), spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontSize=9, fontName="Helvetica-Bold", textColor=colors.HexColor('#64748B'), spaceAfter=15)
    heading_style = ParagraphStyle('SectionHeading', parent=styles['Heading2'], fontSize=12, leading=15, textColor=colors.HexColor('#0F172A'), spaceBefore=14, spaceAfter=6)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['BodyText'], fontSize=10, leading=14, spaceAfter=10)
    
    # --- PAGE 1: EXECUTIVE TEXT SUMMARY COMPONENT ---
    story.append(Paragraph("AETHER SYSTEMS — ENTERPRISE INFRASTRUCTURE REPORT", title_style))
    story.append(Paragraph("[CLASSIFICATION: INTERNAL CORPORATE OPERATIONS TIER]", subtitle_style))
    story.append(Spacer(1, 5))
    
    story.append(Paragraph("1. OPERATIONAL LANDSCAPE EXCERPT", heading_style))
    story.append(Paragraph(
        "During the recent operational auditing sequence, Aether Systems successfully scaled its production "
        "framework clusters. Driven by a global transition toward modular edge deployments, our network core "
        "minimized average database lookup overheads. Localized endpoint configurations successfully processed "
        "massive data sequences without observing structural pipeline drops, securing a 94.2% stability index.", body_style
    ))
    story.append(Paragraph(
        "Our data governance architecture remains fully synchronized across all active multi-tenant container "
        "arrays. System diagnostics confirm that transaction execution tracking speeds normalized back to baseline parameters "
        "following automated microservices cluster balancing optimizations.", body_style
    ))
    
    # --- PAGE 2: METRICS DATA TABLE COMPONENT ---
    story.append(PageBreak()) # Forces data to flow onto Page 2 to test frontend graph pagination layout
    story.append(Paragraph("2. REGIONAL METRIC INGESTION TRACKING", heading_style))
    story.append(Paragraph(
        "The following multi-column relational data matrix details active payload clusters, primary operational gateway "
        "routing checkpoints, and exact volume logging tracking sequences across our framework:", body_style
    ))
    
    table_data = [
        ['Infrastructure Gateway Node', 'Assigned Cluster Core', 'Telemetry Status'],
        ['Gateway Ingress Core Alpha', 'Public Web DMZ Array', '98.4% Efficiency'],
        ['Checkout Verification API', 'Customer Transaction Layer', '142,500 Active Logs'],
        ['Remote VPN Transit Relay', 'Internal Operations Pool', '89,210 Active Logs'],
        ['Corporate Mail Routing Hub', 'Security Filtering Proxy', '12,450 Active Logs']
    ]
    
    data_table = Table(table_data, colWidths=[200, 180, 140])
    data_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F8FAFC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('FONTSIZE', (0,0), (-1,-1), 9.5),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))
    story.append(data_table)
    
    # --- PAGE 3: COMPLEX INFRASTRUCTURE ANALYTICS ---
    story.append(PageBreak()) # Forces data to flow onto Page 3
    story.append(Paragraph("3. SYSTEM STAGING RECONCILIATION ANALYTICS", heading_style))
    story.append(Paragraph(
        "An empirical analysis of our container orchestration configurations isolates a temporary latency profile extension. "
        "Remediation intervals for critical workflow parameters temporarily extended out to an unexpected interval of 18 days "
        "due to deep structural dependency mismatches inside legacy runtime modules.", body_style
    ))
    story.append(Paragraph(
        "Processing processing thresholds immediately normalized down to a fast baseline of 42ms following our cluster "
        "migration to native Kubernetes microservices frameworks. System load curves indicate total processing backlogs "
        "fell by a massive 32.4% following deployment verification parameters.", body_style
    ))
    
    doc.build(story)
    print(f"\n[DATA GENERATION SUCCESS]: Compiled '{filename}' with multi-page textual metrics.")

if __name__ == "__main__":
    build_multipage_dataset()
