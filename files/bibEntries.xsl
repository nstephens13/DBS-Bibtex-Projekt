<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:output method="html" version="4.0" indent="yes" />
    <xsl:template match="/">
            <html>
              <head></head>
              <body>
                 <xsl:apply-templates/>
              </body>
            </html>
      </xsl:template>
    <xsl:template match="/bibliography">
        <h1><xsl:value-of select="title" /></h1>
        <h2><xsl:value-of select="author" /></h2>
        <xsl:apply-templates select="bibentries" />
    </xsl:template>
    <xsl:template match="bibentries">
        <div style="width:100%;vertical-align:top">
            <xsl:apply-templates select="bibentry" />
        </div>
    </xsl:template>
    <xsl:template match="bibentry">
        <div style="width:100%;vertical-align:top">
            <h2><xsl:value-of select="title" /></h2>
            <h4>Type: <xsl:value-of select="@type" /></h4>
            <h4>ID: <xsl:value-of select="@id" /></h4>
            
            <h4>Author: <xsl:value-of select="author" /></h4>
            <h4>Year: <xsl:value-of select="year" /></h4>
            <xsl:if test="publisher">
                <h4>Publisher: <xsl:value-of select="publisher" /></h4>
            </xsl:if>
            <xsl:if test="journal">
                <h4>Journal: <xsl:value-of select="journal" /></h4>
            </xsl:if>
            <xsl:if test="volume">
                <h4>Volume: <xsl:value-of select="volume" /></h4>
            </xsl:if>
            <xsl:if test="number">
                <h4>Number: <xsl:value-of select="number" /></h4>
            </xsl:if>
            <xsl:if test="pages">
                <h4>Pages: <xsl:value-of select="pages" /></h4>
            </xsl:if>
            <xsl:if test="month">
                <h4>Month: <xsl:value-of select="month" /></h4>
            </xsl:if>
            <xsl:if test="note">
                <h4>Note: <xsl:value-of select="note" /></h4>
            </xsl:if>
            <xsl:if test="series">
                <h4>Series: <xsl:value-of select="series" /></h4>
            </xsl:if>
        </div>
    </xsl:template>
</xsl:stylesheet>
