<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="4.0" indent="yes" />
    <xsl:template match="/">
        <html>
            <head />
            <body style="margin: 0 auto; width: 70%; background-image: url('paper_background_1.jpg');">
                <div style="background-color: white; margin: 5px 5px 5px 5px;">
                    <xsl:apply-templates />
                </div>
            </body>
        </html>
    </xsl:template>
    <xsl:template match="/bibliography">
        <div style="margin: 25px 25px 25px 25px;">
            <div style="width:100%; display:flex; align-items: center;">
                <div style="width: 30%;">
                    <img src="wislogo.svg" alt="WisLogo" style="width: 300px; height: 100px;" />
                </div>
            </div>
            <h1>
                <xsl:value-of select="bibtitle" />
            </h1>
            <h3>
                <xsl:value-of select="author" />
            </h3>
            <h1>
                Abstract</h1>
            <p><b>
                    <xsl:value-of select="author" />
                </b> collaborate on a project focusing
            on extracting BibTeX data from <b>
                    <xsl:value-of select="bibtitle" />
                </b> and utilizing Excel for
            organization. The study aims to leverage XSLT to create a visually impactful representation,
            unraveling patterns within the dataset and contributing valuable insights to our field of
            interest.</p>
            <h1>
                References</h1>
            <xsl:apply-templates
                select="bibentries" />
        </div>
    </xsl:template>
    <xsl:template match="bibentries">
        <div style="width:100%;vertical-align:top">
            <xsl:apply-templates select="bibentry" />
        </div>
    </xsl:template>
    <xsl:template match="bibentry">
        <div style="width:100%;">
            <div style="display: grid; grid-template-columns: 20rem auto;">
                <div> [ <span>
                        <xsl:value-of select="@id" />
                    </span> ] </div>
                <div style="margin-left: 1rem;">
                    <span>
                        <xsl:value-of select="author" />
                    </span>
                    <span style="font-style: italic;">, <xsl:value-of select="title" />
                    </span>
                    <span>, (<xsl:value-of select="year" />) </span>
                    <xsl:if test="publisher">
                        <span>, <xsl:value-of select="publisher" />
                        </span>
                    </xsl:if>
                    <xsl:if test="journal">
                        <span>, <xsl:value-of select="journal" />
                        </span>
                    </xsl:if>
                    <xsl:if test="volume">
                        <span>, <xsl:value-of select="volume" />
                        </span>
                    </xsl:if>
                    <xsl:if test="number">
                        <span>, <xsl:value-of select="number" />
                        </span>
                    </xsl:if>
                    <xsl:if test="pages">
                        <span>, <xsl:value-of select="pages" />
                        </span>
                    </xsl:if>
                    <xsl:if test="month">
                        <span>, <xsl:value-of select="month" />
                        </span>
                    </xsl:if>
                    <xsl:if test="note">
                        <span>, <xsl:value-of select="note" />
                        </span>
                    </xsl:if>
                    <xsl:if test="series">
                        <span>, <xsl:value-of select="series" />
                        </span>
                    </xsl:if>
                </div>
            </div>
        </div>
    </xsl:template>
</xsl:stylesheet>
