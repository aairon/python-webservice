def var cSessionParam as char .
def var outfile as char init "/tmp/sys-ctl.json".
pause 0.
assign cSessionParam = session:parameter.

display cSessionParam . 
unix silent value("rm " + outfile) . 

DEF TEMP-TABLE sysCtl LIKE sys-ctl.
 
FOR EACH sys-ctl no-lock where 
	sys-ctl.typ begins cSessionParam : 
    	CREATE sysCtl.
    	BUFFER-COPY sys-ctl TO sysCtl.
END.
 
TEMP-TABLE sysCtl:WRITE-JSON("file", outfile, true, ?).

unix silent value("sed -f sed.sed /tmp/sys-ctl.json > /tmp/sys-ctl.json.tmp ; cp /tmp/sys-ctl.json.tmp /tmp/sys-ctl.json"). 

quit .
/*unix less /tmp/sys-ctl.xml . */
