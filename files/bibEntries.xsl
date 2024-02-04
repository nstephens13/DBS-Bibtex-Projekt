<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="4.0" indent="yes" />
    <xsl:template match="/">
        <html>
            <head />
            <body>
                <xsl:apply-templates />
            </body>
        </html>
    </xsl:template>
    <xsl:template match="/bibliography">
        <div style="width:100%; display:flex;">
            <div style="width: 30%;">
                <img src="wislogo.svg" alt="WisLogo" style="width: 300px; height: 100px;" />
            </div>
            <div style="width:70%; margin-left: 1rem; align-text: ">
                <h1>
                    <xsl:value-of select="bibtitle" />
                </h1>
                <h2><xsl:value-of select="author" /></h2>
            </div>
        </div>
        <h1>References</h1>
        <xsl:apply-templates
            select="bibentries" />
    </xsl:template>
    <xsl:template match="bibentries">
        <div style="width:100%;vertical-align:top">
            <xsl:apply-templates select="bibentry" />
        </div>
    </xsl:template>
    <xsl:template match="bibentry">
        <div style="width:100%;">
            <div style="width:100%; display:flex;">
                <div style="width:10rem;">
                    [ <span><xsl:value-of select="@type" /> </span> ]
                </div>
                <div style="margin-left: 1rem;">
                    <span style="font-style: italic;">
                        <xsl:value-of select="title" />
                    </span>
                    <span>Type: <xsl:value-of select="@type" />
                    </span>
                    <span>Author: <xsl:value-of select="author" />
                    </span>
                    <span>Year: <xsl:value-of select="year" />
                    </span>
                </div>
            </div>
            <!--
            <xsl:if test="publisher">
                <span>Publisher: <xsl:value-of select="publisher" />
                </span>
            </xsl:if>
            <xsl:if test="journal">
                <span>Journal: <xsl:value-of select="journal" />
                </span>
            </xsl:if>
            <xsl:if test="volume">
                <span>Volume: <xsl:value-of select="volume" />
                </span>
            </xsl:if>
            <xsl:if test="number">
                <span>Number: <xsl:value-of select="number" />
                </span>
            </xsl:if>
            <xsl:if test="pages">
                <span>Pages: <xsl:value-of select="pages" />
                </span>
            </xsl:if>
            <xsl:if test="month">
                <span>Month: <xsl:value-of select="month" />
                </span>
            </xsl:if>
            <xsl:if test="note">
                <span>Note: <xsl:value-of select="note" />
                </span>
            </xsl:if>
            <xsl:if test="series">
                <span>Series: <xsl:value-of select="series" />
                </span>
            </xsl:if>
             -->
        </div>
    </xsl:template>
</xsl:stylesheet>