def var cSessionParam as char .
assign cSessionParam = session:parameter.

DEFINE VARIABLE cTargetType AS CHARACTER NO-UNDO.
DEFINE VARIABLE cFile       AS CHARACTER NO-UNDO.
DEFINE VARIABLE lFormatted  AS LOGICAL   NO-UNDO.
DEFINE VARIABLE lRetOK      AS LOGICAL   NO-UNDO.

def var cEncoding 		as char init ?  .
def var cSchemaLocation 	as char init ?	.
def var lWriteSchema 		as log  init FALSE.
def var lMinSchema 		as log  init FALSE.
def var lWriteBeforeImage 	as log  init FALSE.

DEFINE TEMP-TABLE ttcust NO-UNDO LIKE cust .
DEFINE TEMP-TABLE ttcust-job    NO-UNDO LIKE cust-job .
DEFINE TEMP-TABLE ttprc-hdr  NO-UNDO LIKE prc-hdr .

DEFINE DATASET dscust-jobLog FOR ttcust, ttcust-job, ttprc-hdr
  DATA-RELATION CustOrd FOR ttcust,
    ttcust-job RELATION-FIELDS(acct-nbr,acct-nbr) NESTED
  DATA-RELATION OrdInv FOR ttcust-job,
    ttprc-hdr RELATION-FIELDS(job-nbr,job-nbr) NESTED.

DEFINE DATA-SOURCE dscust FOR cust.
DEFINE DATA-SOURCE dscust-job    FOR cust-job.
DEFINE DATA-SOURCE dsprc-hdr  FOR prc-hdr.

BUFFER ttcust:HANDLE:ATTACH-DATA-SOURCE(DATA-SOURCE dscust:HANDLE).
BUFFER ttcust-job:HANDLE:ATTACH-DATA-SOURCE(DATA-SOURCE dscust-job:HANDLE).
BUFFER ttprc-hdr:HANDLE:ATTACH-DATA-SOURCE(DATA-SOURCE dsprc-hdr:HANDLE).

DATA-SOURCE dscust:FILL-WHERE-STRING = "WHERE cust.acct-nbr = " + string(int(cSessionParam)) .
DATASET dscust-jobLog:FILL().

ASSIGN
  cTargetType = "file"
  cFile       = "dset.json"
  lFormatted  = TRUE.

/*lRetOK = DATASET dscust-jobLog:WRITE-JSON(cTargetType, cFile, lFormatted). */

ASSIGN
	cTargetType = "FILE"
	cFile = "/tmp/cust.xml"
	lFormatted = TRUE
	cEncoding = ?
	cSchemaLocation = ?
	lWriteSchema = FALSE
	lMinSchema = FALSE
	lWriteBeforeImage = FALSE.

lRetOK = DATASET dscust-jobLog:WRITE-XML(cTargetType, cFile, lFormatted,
cEncoding, cSchemaLocation, lMinSchema, lWriteBeforeImage). 

quit.
