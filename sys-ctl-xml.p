def var cSessionParam as char .
assign cSessionParam = session:parameter.

unix silent value("rm /tmp/sys-ctl.xml").

DEF TEMP-TABLE stt LIKE sys-ctl.
 
FOR EACH sys-ctl no-lock where 
	sys-ctl.typ begins cSessionParam : 
    	CREATE stt.
    	BUFFER-COPY sys-ctl TO stt.
END.
 
TEMP-TABLE stt:WRITE-XML("file", "/tmp/sys-ctl.xml", true, ?, ?, FALSE, TRUE).

quit .
/*unix less /tmp/sys-ctl.xml . */
