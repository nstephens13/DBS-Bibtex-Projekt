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
            <h2>Title: <xsl:value-of select="title" /></h2>
            <h4>Type: <xsl:value-of select="@type" /></h4>
            <h4>ID: <xsl:value-of select="@id" /></h4>
            <xsl:choose>
            <xsl:when test="name()='author'">
                <!-- Apply design for author -->
                <strong style="color: red;"><xsl:value-of select="author()" /></strong>: <xsl:value-of select="." />
            </xsl:when>
            <xsl:when test="name()='year'">
                <!-- Apply design for field2 -->
                <strong style="color: blue;"><xsl:value-of select="year()" /></strong>: <xsl:value-of select="." />
            </xsl:when>
            <xsl:otherwise>
                <!-- Default design -->
                <strong><xsl:value-of select="name()" /></strong>: <xsl:value-of select="." />
            </xsl:otherwise>
        </xsl:choose>
    </div>
    </xsl:template>
</xsl:stylesheet>