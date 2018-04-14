def var cSessionParam as char .
assign cSessionParam = session:parameter.

display cSessionParam . 

unix silent value("rm /tmp/sys-ctl.json").

DEF TEMP-TABLE stt LIKE sys-ctl.
 
FOR EACH sys-ctl no-lock where 
	sys-ctl.typ begins cSessionParam : 
    	CREATE stt.
    	BUFFER-COPY sys-ctl TO stt.
END.
 
TEMP-TABLE stt:WRITE-JSON("file", "/tmp/sys-ctl.json", true).

quit .
/*unix less /tmp/sys-ctl.xml . */
