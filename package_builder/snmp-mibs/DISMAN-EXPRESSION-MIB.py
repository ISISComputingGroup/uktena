# SNMP MIB module (DISMAN-EXPRESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source https://raw.githubusercontent.com/net-snmp/net-snmp/master/mibs/DISMAN-EXPRESSION-MIB.txt
# Produced by pysmi-1.4.3 at Wed Apr 10 12:56:21 2024
# On host ? platform ? version ? by user ?
# Using Python version 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(NotificationGroup,
 ModuleCompliance,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

(ObjectIdentity,
 Counter64,
 Gauge32,
 Bits,
 mib_2,
 TimeTicks,
 NotificationType,
 MibIdentifier,
 Integer32,
 iso,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 zeroDotZero,
 IpAddress,
 ModuleIdentity,
 Counter32,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "ObjectIdentity",
    "Counter64",
    "Gauge32",
    "Bits",
    "mib-2",
    "TimeTicks",
    "NotificationType",
    "MibIdentifier",
    "Integer32",
    "iso",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "zeroDotZero",
    "IpAddress",
    "ModuleIdentity",
    "Counter32",
    "Unsigned32")

(RowStatus,
 TimeStamp,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "RowStatus",
    "TimeStamp",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dismanExpressionMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 90)
)
dismanExpressionMIB.setRevisions(
        ("2000-10-16 00:00",)
)
dismanExpressionMIB.setLastUpdated("200010160000Z")
if mibBuilder.loadTexts:
    dismanExpressionMIB.setOrganization("""\
IETF Distributed Management Working Group
""")
dismanExpressionMIB.setContactInfo("""\
Ramanathan Kavasseri
                  Cisco Systems, Inc.
                  170 West Tasman Drive,
                  San Jose CA 95134-1706.
                  Phone: +1 408 527 2446
                  Email: ramk@cisco.com
""")
if mibBuilder.loadTexts:
    dismanExpressionMIB.setDescription("""\
The MIB module for defining expressions of MIB objects for
     management purposes.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysUpTimeInstance_ObjectIdentity = ObjectIdentity
sysUpTimeInstance = _SysUpTimeInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 3, 0)
)
_DismanExpressionMIBObjects_ObjectIdentity = ObjectIdentity
dismanExpressionMIBObjects = _DismanExpressionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1)
)
_ExpResource_ObjectIdentity = ObjectIdentity
expResource = _ExpResource_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1, 1)
)


class _ExpResourceDeltaMinimum_Type(Integer32):
    """Custom type expResourceDeltaMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 600),
    )


_ExpResourceDeltaMinimum_Type.__name__ = "Integer32"
_ExpResourceDeltaMinimum_Object = MibScalar
expResourceDeltaMinimum = _ExpResourceDeltaMinimum_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 1),
    _ExpResourceDeltaMinimum_Type()
)
expResourceDeltaMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expResourceDeltaMinimum.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaMinimum.setUnits("seconds")
if mibBuilder.loadTexts:
    expResourceDeltaMinimum.setDescription("""\
The minimum expExpressionDeltaInterval this system will
     accept.  A system may use the larger values of this minimum to
     lessen the impact of constantly computing deltas.  For larger
     delta sampling intervals the system samples less often and
     suffers less overhead.  This object provides a way to enforce
     such lower overhead for all expressions created after it is
     set.

     The value -1 indicates that expResourceDeltaMinimum is
     irrelevant as the system will not accept 'deltaValue' as a
     value for expObjectSampleType.

     Unless explicitly resource limited, a system's value for
     this object should be 1, allowing as small as a 1 second
     interval for ongoing delta sampling.

     Changing this value will not invalidate an existing setting
     of expObjectSampleType.
""")
_ExpResourceDeltaWildcardInstanceMaximum_Type = Unsigned32
_ExpResourceDeltaWildcardInstanceMaximum_Object = MibScalar
expResourceDeltaWildcardInstanceMaximum = _ExpResourceDeltaWildcardInstanceMaximum_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 2),
    _ExpResourceDeltaWildcardInstanceMaximum_Type()
)
expResourceDeltaWildcardInstanceMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceMaximum.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceMaximum.setUnits("instances")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceMaximum.setDescription("""\
For every instance of a deltaValue object, one dynamic instance
     entry is needed for holding the instance value from the previous
     sample, i.e. to maintain state.

     This object limits maximum number of dynamic instance entries
     this system will support for wildcarded delta objects in
     expressions. For a given delta expression, the number of
     dynamic instances is the number of values that meet all criteria
     to exist times the number of delta values in the expression.

     A value of 0 indicates no preset limit, that is, the limit
     is dynamic based on system operation and resources.

     Unless explicitly resource limited, a system's value for
     this object should be 0.

     Changing this value will not eliminate or inhibit existing delta
     wildcard instance objects but will prevent the creation of more
     such objects.

     An attempt to allocate beyond the limit results in expErrorCode
     being tooManyWildcardValues for that evaluation attempt.
""")
_ExpResourceDeltaWildcardInstances_Type = Gauge32
_ExpResourceDeltaWildcardInstances_Object = MibScalar
expResourceDeltaWildcardInstances = _ExpResourceDeltaWildcardInstances_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 3),
    _ExpResourceDeltaWildcardInstances_Type()
)
expResourceDeltaWildcardInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstances.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstances.setUnits("instances")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstances.setDescription("""\
The number of currently active instance entries as
     defined for expResourceDeltaWildcardInstanceMaximum.
""")
_ExpResourceDeltaWildcardInstancesHigh_Type = Gauge32
_ExpResourceDeltaWildcardInstancesHigh_Object = MibScalar
expResourceDeltaWildcardInstancesHigh = _ExpResourceDeltaWildcardInstancesHigh_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 4),
    _ExpResourceDeltaWildcardInstancesHigh_Type()
)
expResourceDeltaWildcardInstancesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstancesHigh.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstancesHigh.setUnits("instances")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstancesHigh.setDescription("""\
The highest value of expResourceDeltaWildcardInstances
     that has occurred since initialization of the managed
     system.
""")
_ExpResourceDeltaWildcardInstanceResourceLacks_Type = Counter32
_ExpResourceDeltaWildcardInstanceResourceLacks_Object = MibScalar
expResourceDeltaWildcardInstanceResourceLacks = _ExpResourceDeltaWildcardInstanceResourceLacks_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 1, 5),
    _ExpResourceDeltaWildcardInstanceResourceLacks_Type()
)
expResourceDeltaWildcardInstanceResourceLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceResourceLacks.setStatus("current")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceResourceLacks.setUnits("instances")
if mibBuilder.loadTexts:
    expResourceDeltaWildcardInstanceResourceLacks.setDescription("""\
The number of times this system could not evaluate an
     expression because that would have created a value instance in
     excess of expResourceDeltaWildcardInstanceMaximum.
""")
_ExpDefine_ObjectIdentity = ObjectIdentity
expDefine = _ExpDefine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1, 2)
)
_ExpExpressionTable_Object = MibTable
expExpressionTable = _ExpExpressionTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1)
)
if mibBuilder.loadTexts:
    expExpressionTable.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionTable.setDescription("""\
A table of expression definitions.
""")
_ExpExpressionEntry_Object = MibTableRow
expExpressionEntry = _ExpExpressionEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1)
)
expExpressionEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
)
if mibBuilder.loadTexts:
    expExpressionEntry.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionEntry.setDescription("""\
Information about a single expression.  New expressions
     can be created using expExpressionRowStatus.

     To create an expression first create the named entry in this
     table.  Then use expExpressionName to populate expObjectTable.
     For expression evaluation to succeed all related entries in
     expExpressionTable and expObjectTable must be 'active'.  If
     these conditions are not met the corresponding values in
     expValue simply are not instantiated.

     Deleting an entry deletes all related entries in expObjectTable
     and expErrorTable.

     Because of the relationships among the multiple tables for an
     expression (expExpressionTable, expObjectTable, and
     expValueTable) and the SNMP rules for independence in setting
     object values, it is necessary to do final error checking when
     an expression is evaluated, that is, when one of its instances
     in expValueTable is read or a delta interval expires.  Earlier
     checking need not be done and an implementation may not impose
     any ordering on the creation of objects related to an
     expression.

     To maintain security of MIB information, when creating a new row in
     this table, the managed system must record the security credentials
     of the requester.  These security credentials are the parameters
     necessary as inputs to isAccessAllowed from the Architecture for

     Describing SNMP Management Frameworks.  When obtaining the objects
     that make up the expression, the system must (conceptually) use
     isAccessAllowed to ensure that it does not violate security.

     The evaluation of the expression takes place under the
     security credentials of the creator of its expExpressionEntry.

     Values of read-write objects in this table may be changed

     at any time.
""")


class _ExpExpressionOwner_Type(SnmpAdminString):
    """Custom type expExpressionOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExpExpressionOwner_Type.__name__ = "SnmpAdminString"
_ExpExpressionOwner_Object = MibTableColumn
expExpressionOwner = _ExpExpressionOwner_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 1),
    _ExpExpressionOwner_Type()
)
expExpressionOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expExpressionOwner.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionOwner.setDescription("""\
The owner of this entry. The exact semantics of this
     string are subject to the security policy defined by the
     security administrator.
""")


class _ExpExpressionName_Type(SnmpAdminString):
    """Custom type expExpressionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExpExpressionName_Type.__name__ = "SnmpAdminString"
_ExpExpressionName_Object = MibTableColumn
expExpressionName = _ExpExpressionName_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 2),
    _ExpExpressionName_Type()
)
expExpressionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expExpressionName.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionName.setDescription("""\
The name of the expression.  This is locally unique, within
     the scope of an expExpressionOwner.
""")


class _ExpExpression_Type(OctetString):
    """Custom type expExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_ExpExpression_Type.__name__ = "OctetString"
_ExpExpression_Object = MibTableColumn
expExpression = _ExpExpression_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 3),
    _ExpExpression_Type()
)
expExpression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpression.setStatus("current")
if mibBuilder.loadTexts:
    expExpression.setDescription("""\
The expression to be evaluated.  This object is the same
     as a DisplayString (RFC 1903) except for its maximum length.

     Except for the variable names the expression is in ANSI C
     syntax.  Only the subset of ANSI C operators and functions
     listed here is allowed.

     Variables are expressed as a dollar sign ('$') and an

     integer that corresponds to an expObjectIndex.  An
     example of a valid expression is:

          ($1-$5)*100

     Expressions must not be recursive, that is although an expression
     may use the results of another expression, it must not contain
     any variable that is directly or indirectly a result of its own
     evaluation. The managed system must check for recursive
     expressions.

     The only allowed operators are:

          ( )
          - (unary)
          + - * / %
          & | ^ << >> ~
          ! && || == != > >= < <=

     Note the parentheses are included for parenthesizing the
     expression, not for casting data types.

     The only constant types defined are:

          int (32-bit signed)
          long (64-bit signed)
          unsigned int
          unsigned long
          hexadecimal
          character
          string
          oid

     The default type for a positive integer is int unless it is too
     large in which case it is long.

     All but oid are as defined for ANSI C.  Note that a
     hexadecimal constant may end up as a scalar or an array of
     8-bit integers.  A string constant is enclosed in double
     quotes and may contain back-slashed individual characters
     as in ANSI C.

     An oid constant comprises 32-bit, unsigned integers and at
     least one period, for example:

          0.
          .0
          1.3.6.1

     No additional leading or trailing subidentifiers are automatically
     added to an OID constant.  The constant is taken as expressed.

     Integer-typed objects are treated as 32- or 64-bit, signed
     or unsigned integers, as appropriate.  The results of
     mixing them are as for ANSI C, including the type of the
     result.  Note that a 32-bit value is thus promoted to 64 bits
     only in an operation with a 64-bit value.  There is no
     provision for larger values to handle overflow.

     Relative to SNMP data types, a resulting value becomes
     unsigned when calculating it uses any unsigned value,
     including a counter.  To force the final value to be of
     data type counter the expression must explicitly use the
     counter32() or counter64() function (defined below).

     OCTET STRINGS and OBJECT IDENTIFIERs are treated as
     one-dimensioned arrays of unsigned 8-bit integers and
     unsigned 32-bit integers, respectively.

     IpAddresses are treated as 32-bit, unsigned integers in
     network byte order, that is, the hex version of 255.0.0.0 is
     0xff000000.

     Conditional expressions result in a 32-bit, unsigned integer
     of value 0 for false or 1 for true. When an arbitrary value
     is used as a boolean 0 is false and non-zero is true.

     Rules for the resulting data type from an operation, based on
     the operator:

     For << and >> the result is the same as the left hand operand.

     For &&, ||, ==, !=, <, <=, >, and >= the result is always
     Unsigned32.

     For unary - the result is always Integer32.

     For +, -, *, /, %, &, |, and ^ the result is promoted according
     to the following rules, in order from most to least preferred:

          If left hand and right hand operands are the same type,
          use that.

          If either side is Counter64, use that.

          If either side is IpAddress, use that.

          If either side is TimeTicks, use that.

          If either side is Counter32, use that.

          Otherwise use Unsigned32.

     The following rules say what operators apply with what data
     types.  Any combination not explicitly defined does not work.

     For all operators any of the following can be the left hand or
     right hand operand: Integer32, Counter32, Unsigned32, Counter64.

     The operators +, -, *, /, %, <, <=, >, and >= work with
     TimeTicks.

     The operators &, |, and ^ work with IpAddress.

     The operators << and >> work with IpAddress but only as the
     left hand operand.

     The + operator performs a concatenation of two OCTET STRINGs or
     two OBJECT IDENTIFIERs.

     The operators &, | perform bitwise operations on OCTET STRINGs.
     If the OCTET STRING happens to be a DisplayString the results
     may be meaningless, but the agent system does not check this as
     some such systems do not have this information.

     The operators << and >> perform bitwise operations on OCTET
     STRINGs appearing as the left hand operand.

     The only functions defined are:

          counter32
          counter64
          arraySection
          stringBegins
          stringEnds
          stringContains
          oidBegins
          oidEnds
          oidContains
          average
          maximum
          minimum
          sum
          exists

     The following function definitions indicate their parameters by
     naming the data type of the parameter in the parameter's position
     in the parameter list.  The parameter must be of the type indicated
     and generally may be a constant, a MIB object, a function, or an
     expression.

     counter32(integer) - wrapped around an integer value counter32
     forces Counter32 as a data type.

     counter64(integer) - similar to counter32 except that the
     resulting data type is 'counter64'.

     arraySection(array, integer, integer) - selects a piece of an
     array (i.e. part of an OCTET STRING or OBJECT IDENTIFIER).  The
     integer arguments are in the range 0 to 4,294,967,295.  The
     first is an initial array index (one-dimensioned) and the second
     is an ending array index.  A value of 0 indicates first or last
     element, respectively.  If the first element is larger than the
     array length the result is 0 length.  If the second integer is
     less than or equal to the first, the result is 0 length.  If the
     second is larger than the array length it indicates last
     element.

     stringBegins/Ends/Contains(octetString, octetString) - looks for
     the second string (which can be a string constant) in the first
     and returns the one-dimensioned arrayindex where the match began.
     A return value of 0 indicates no match (i.e. boolean false).

     oidBegins/Ends/Contains(oid, oid) - looks for the second OID
     (which can be an OID constant) in the first and returns the
     the one-dimensioned index where the match began. A return value
     of 0 indicates no match (i.e. boolean false).

     average/maximum/minimum(integer) - calculates the average,
     minimum, or maximum value of the integer valued object over
     multiple sample times.  If the object disappears for any
     sample period, the accumulation and the resulting value object
     cease to exist until the object reappears at which point the
     calculation starts over.

     sum(integerObject*) - sums all available values of the
     wildcarded integer object, resulting in an integer scalar.  Must
     be used with caution as it wraps on overflow with no
     notification.

     exists(anyTypeObject) - verifies the object instance exists. A
     return value of 0 indicates NoSuchInstance (i.e. boolean
     false).
""")


class _ExpExpressionValueType_Type(Integer32):
    """Custom type expExpressionValueType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 1),
          ("counter64", 8),
          ("integer32", 4),
          ("ipAddress", 5),
          ("objectId", 7),
          ("octetString", 6),
          ("timeTicks", 3),
          ("unsigned32", 2))
    )


_ExpExpressionValueType_Type.__name__ = "Integer32"
_ExpExpressionValueType_Object = MibTableColumn
expExpressionValueType = _ExpExpressionValueType_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 4),
    _ExpExpressionValueType_Type()
)
expExpressionValueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionValueType.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionValueType.setDescription("""\
The type of the expression value.  One and only one of the
     value objects in expValueTable will be instantiated to match
     this type.

     If the result of the expression can not be made into this type,
     an invalidOperandType error will occur.
""")


class _ExpExpressionComment_Type(SnmpAdminString):
    """Custom type expExpressionComment based on SnmpAdminString"""
    defaultHexValue = ""


_ExpExpressionComment_Object = MibTableColumn
expExpressionComment = _ExpExpressionComment_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 5),
    _ExpExpressionComment_Type()
)
expExpressionComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionComment.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionComment.setDescription("""\
A comment to explain the use or meaning of the expression.
""")


class _ExpExpressionDeltaInterval_Type(Integer32):
    """Custom type expExpressionDeltaInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ExpExpressionDeltaInterval_Type.__name__ = "Integer32"
_ExpExpressionDeltaInterval_Object = MibTableColumn
expExpressionDeltaInterval = _ExpExpressionDeltaInterval_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 6),
    _ExpExpressionDeltaInterval_Type()
)
expExpressionDeltaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionDeltaInterval.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionDeltaInterval.setUnits("seconds")
if mibBuilder.loadTexts:
    expExpressionDeltaInterval.setDescription("""\
Sampling interval for objects in this expression with
     expObjectSampleType 'deltaValue'.

     This object has no effect if the the expression has no
     deltaValue objects.

     A value of 0 indicates no automated sampling.  In this case
     the delta is the difference from the last time the expression
     was evaluated.  Note that this is subject to unpredictable
     delta times in the face of retries or multiple managers.

     A value greater than zero is the number of seconds between
     automated samples.

     Until the delta interval has expired once the delta for the

     object is effectively not instantiated and evaluating
     the expression has results as if the object itself were not
     instantiated.

     Note that delta values potentially consume large amounts of
     system CPU and memory.  Delta state and processing must
     continue constantly even if the expression is not being used.
     That is, the expression is being evaluated every delta interval,
     even if no application is reading those values.  For wildcarded
     objects this can be substantial overhead.

     Note that delta intervals, external expression value sampling
     intervals and delta intervals for expressions within other
     expressions can have unusual interactions as they are impossible
     to synchronize accurately.  In general one interval embedded
     below another must be enough shorter that the higher sample
     sees relatively smooth, predictable behavior.  So, for example,
     to avoid the higher level getting the same sample twice, the
     lower level should sample at least twice as fast as the higher
     level does.
""")
_ExpExpressionPrefix_Type = ObjectIdentifier
_ExpExpressionPrefix_Object = MibTableColumn
expExpressionPrefix = _ExpExpressionPrefix_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 7),
    _ExpExpressionPrefix_Type()
)
expExpressionPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionPrefix.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionPrefix.setDescription("""\
An object prefix to assist an application in determining
     the instance indexing to use in expValueTable, relieving the
     application of the need to scan the expObjectTable to
     determine such a prefix.

     See expObjectTable for information on wildcarded objects.

     If the expValueInstance portion of the value OID may
     be treated as a scalar (that is, normally, 0) the value of
     expExpressionPrefix is zero length, that is, no OID at all.
     Note that zero length implies a null OID, not the OID 0.0.

     Otherwise, the value of expExpressionPrefix is the expObjectID
     value of any one of the wildcarded objects for the expression.
     This is sufficient, as the remainder, that is, the instance
     fragment relevant to instancing the values, must be the same for
     all wildcarded objects in the expression.
""")
_ExpExpressionErrors_Type = Counter32
_ExpExpressionErrors_Object = MibTableColumn
expExpressionErrors = _ExpExpressionErrors_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 8),
    _ExpExpressionErrors_Type()
)
expExpressionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expExpressionErrors.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionErrors.setDescription("""\
The number of errors encountered while evaluating this
     expression.

     Note that an object in the expression not being accessible,
     is not considered an error. An example of an inaccessible
     object is when the object is excluded from the view of the
     user whose security credentials are used in the expression
     evaluation. In such cases, it is a legitimate condition
     that causes the corresponding expression value not to be
     instantiated.
""")
_ExpExpressionEntryStatus_Type = RowStatus
_ExpExpressionEntryStatus_Object = MibTableColumn
expExpressionEntryStatus = _ExpExpressionEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 1, 1, 9),
    _ExpExpressionEntryStatus_Type()
)
expExpressionEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expExpressionEntryStatus.setStatus("current")
if mibBuilder.loadTexts:
    expExpressionEntryStatus.setDescription("""\
The control that allows creation and deletion of entries.
""")
_ExpErrorTable_Object = MibTable
expErrorTable = _ExpErrorTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2)
)
if mibBuilder.loadTexts:
    expErrorTable.setStatus("current")
if mibBuilder.loadTexts:
    expErrorTable.setDescription("""\
A table of expression errors.
""")
_ExpErrorEntry_Object = MibTableRow
expErrorEntry = _ExpErrorEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1)
)
expErrorEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
)
if mibBuilder.loadTexts:
    expErrorEntry.setStatus("current")
if mibBuilder.loadTexts:
    expErrorEntry.setDescription("""\
Information about errors in processing an expression.

     Entries appear in this table only when there is a matching
     expExpressionEntry and then only when there has been an
     error for that expression as reflected by the error codes
     defined for expErrorCode.
""")
_ExpErrorTime_Type = TimeStamp
_ExpErrorTime_Object = MibTableColumn
expErrorTime = _ExpErrorTime_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 1),
    _ExpErrorTime_Type()
)
expErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorTime.setStatus("current")
if mibBuilder.loadTexts:
    expErrorTime.setDescription("""\
The value of sysUpTime the last time an error caused a
     failure to evaluate this expression.
""")
_ExpErrorIndex_Type = Integer32
_ExpErrorIndex_Object = MibTableColumn
expErrorIndex = _ExpErrorIndex_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 2),
    _ExpErrorIndex_Type()
)
expErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorIndex.setStatus("current")
if mibBuilder.loadTexts:
    expErrorIndex.setDescription("""\
The one-dimensioned character array index into
     expExpression for where the error occurred.  The value
     zero indicates irrelevance.
""")


class _ExpErrorCode_Type(Integer32):
    """Custom type expErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("deltaTooShort", 9),
          ("divideByZero", 11),
          ("invalidOperandType", 5),
          ("invalidSyntax", 1),
          ("recursion", 8),
          ("resourceUnavailable", 10),
          ("tooManyWildcardValues", 7),
          ("undefinedObjectIndex", 2),
          ("unmatchedParenthesis", 6),
          ("unrecognizedFunction", 4),
          ("unrecognizedOperator", 3))
    )


_ExpErrorCode_Type.__name__ = "Integer32"
_ExpErrorCode_Object = MibTableColumn
expErrorCode = _ExpErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 3),
    _ExpErrorCode_Type()
)
expErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorCode.setStatus("current")
if mibBuilder.loadTexts:
    expErrorCode.setDescription("""\
The error that occurred.  In the following explanations the
     expected timing of the error is in parentheses.  'S' means
     the error occurs on a Set request.  'E' means the error

     occurs on the attempt to evaluate the expression either due to
     Get from expValueTable or in ongoing delta processing.

     invalidSyntax       the value sent for expExpression is not
                    valid Expression MIB expression syntax
                    (S)
     undefinedObjectIndex     an object reference ($n) in
                    expExpression does not have a matching
                    instance in expObjectTable (E)
     unrecognizedOperator     the value sent for expExpression held an
                    unrecognized operator (S)
     unrecognizedFunction     the value sent for expExpression held an
                    unrecognized function name (S)
     invalidOperandType  an operand in expExpression is not the
                    right type for the associated operator
                    or result (SE)
     unmatchedParenthesis     the value sent for expExpression is not
                    correctly parenthesized (S)
     tooManyWildcardValues    evaluating the expression exceeded the
                    limit set by
                    expResourceDeltaWildcardInstanceMaximum
                    (E)
     recursion      through some chain of embedded
                    expressions the expression invokes itself
                    (E)
     deltaTooShort       the delta for the next evaluation passed
                    before the system could evaluate the
                    present sample (E)
     resourceUnavailable some resource, typically dynamic memory,
                    was unavailable (SE)
     divideByZero        an attempt to divide by zero occurred
                    (E)

     For the errors that occur when the attempt is made to set
     expExpression Set request fails with the SNMP error code
     'wrongValue'.  Such failures refer to the most recent failure to
     Set expExpression, not to the present value of expExpression
     which must be either unset or syntactically correct.

     Errors that occur during evaluation for a Get* operation return
     the SNMP error code 'genErr' except for 'tooManyWildcardValues'
     and 'resourceUnavailable' which return the SNMP error code
     'resourceUnavailable'.
""")
_ExpErrorInstance_Type = ObjectIdentifier
_ExpErrorInstance_Object = MibTableColumn
expErrorInstance = _ExpErrorInstance_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 2, 1, 4),
    _ExpErrorInstance_Type()
)
expErrorInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expErrorInstance.setStatus("current")
if mibBuilder.loadTexts:
    expErrorInstance.setDescription("""\
The expValueInstance being evaluated when the error
     occurred.  A zero-length indicates irrelevance.
""")
_ExpObjectTable_Object = MibTable
expObjectTable = _ExpObjectTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3)
)
if mibBuilder.loadTexts:
    expObjectTable.setStatus("current")
if mibBuilder.loadTexts:
    expObjectTable.setDescription("""\
A table of object definitions for each expExpression.

     Wildcarding instance IDs:

     It is legal to omit all or part of the instance portion for
     some or all of the objects in an expression. (See the
     DESCRIPTION of expObjectID for details.  However, note that
     if more than one object in the same expression is wildcarded
     in this way, they all must be objects where that portion of
     the instance is the same.  In other words, all objects may be
     in the same SEQUENCE or in different SEQUENCEs but with the
     same semantic index value (e.g., a value of ifIndex)
     for the wildcarded portion.
""")
_ExpObjectEntry_Object = MibTableRow
expObjectEntry = _ExpObjectEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1)
)
expObjectEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
    (0, "DISMAN-EXPRESSION-MIB", "expObjectIndex"),
)
if mibBuilder.loadTexts:
    expObjectEntry.setStatus("current")
if mibBuilder.loadTexts:
    expObjectEntry.setDescription("""\
Information about an object.  An application uses
     expObjectEntryStatus to create entries in this table while
     in the process of defining an expression.

     Values of read-create objects in this table may be
     changed at any time.
""")


class _ExpObjectIndex_Type(Unsigned32):
    """Custom type expObjectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ExpObjectIndex_Type.__name__ = "Unsigned32"
_ExpObjectIndex_Object = MibTableColumn
expObjectIndex = _ExpObjectIndex_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 1),
    _ExpObjectIndex_Type()
)
expObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expObjectIndex.setStatus("current")
if mibBuilder.loadTexts:
    expObjectIndex.setDescription("""\
Within an expression, a unique, numeric identification for an
     object.  Prefixed with a dollar sign ('$') this is used to
     reference the object in the corresponding expExpression.
""")
_ExpObjectID_Type = ObjectIdentifier
_ExpObjectID_Object = MibTableColumn
expObjectID = _ExpObjectID_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 2),
    _ExpObjectID_Type()
)
expObjectID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectID.setStatus("current")
if mibBuilder.loadTexts:
    expObjectID.setDescription("""\
The OBJECT IDENTIFIER (OID) of this object.  The OID may be
     fully qualified, meaning it includes a complete instance
     identifier part (e.g., ifInOctets.1 or sysUpTime.0), or it
     may not be fully qualified, meaning it may lack all or part
     of the instance identifier.  If the expObjectID is not fully
     qualified, then expObjectWildcard must be set to true(1).
     The value of the expression will be multiple
     values, as if done for a GetNext sweep of the object.

     An object here may itself be the result of an expression but
     recursion is not allowed.

     NOTE:  The simplest implementations of this MIB may not allow
     wildcards.
""")


class _ExpObjectIDWildcard_Type(TruthValue):
    """Custom type expObjectIDWildcard based on TruthValue"""


_ExpObjectIDWildcard_Object = MibTableColumn
expObjectIDWildcard = _ExpObjectIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 3),
    _ExpObjectIDWildcard_Type()
)
expObjectIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectIDWildcard.setStatus("current")
if mibBuilder.loadTexts:
    expObjectIDWildcard.setDescription("""\
A true value indicates the expObjecID of this row is a wildcard
        object. False indicates that expObjectID is fully instanced.
        If all expObjectWildcard values for a given expression are FALSE,
        expExpressionPrefix will reflect a scalar object (i.e. will
        be 0.0).

        NOTE:  The simplest implementations of this MIB may not allow
        wildcards.
""")


class _ExpObjectSampleType_Type(Integer32):
    """Custom type expObjectSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("changedValue", 3),
          ("deltaValue", 2))
    )


_ExpObjectSampleType_Type.__name__ = "Integer32"
_ExpObjectSampleType_Object = MibTableColumn
expObjectSampleType = _ExpObjectSampleType_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 4),
    _ExpObjectSampleType_Type()
)
expObjectSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectSampleType.setStatus("current")
if mibBuilder.loadTexts:
    expObjectSampleType.setDescription("""\
The method of sampling the selected variable.

     An 'absoluteValue' is simply the present value of the object.

     A 'deltaValue' is the present value minus the previous value,
     which was sampled expExpressionDeltaInterval seconds ago.
     This is intended primarily for use with SNMP counters, which are
     meaningless as an 'absoluteValue', but may be used with any
     integer-based value.

     A 'changedValue' is a boolean for whether the present value is
     different from the previous value.  It is applicable to any data
     type and results in an Unsigned32 with value 1 if the object's
     value is changed and 0 if not.  In all other respects it is as a
     'deltaValue' and all statements and operation regarding delta
     values apply to changed values.

     When an expression contains both delta and absolute values
     the absolute values are obtained at the end of the delta
     period.
""")


class _ExpObjectDeltaDiscontinuityID_Type(ObjectIdentifier):
    """Custom type expObjectDeltaDiscontinuityID based on ObjectIdentifier"""
    defaultValue = "(1, 3, 6, 1, 2, 1, 1, 3, 0)"


_ExpObjectDeltaDiscontinuityID_Object = MibTableColumn
expObjectDeltaDiscontinuityID = _ExpObjectDeltaDiscontinuityID_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 5),
    _ExpObjectDeltaDiscontinuityID_Type()
)
expObjectDeltaDiscontinuityID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectDeltaDiscontinuityID.setStatus("current")
if mibBuilder.loadTexts:
    expObjectDeltaDiscontinuityID.setDescription("""\
The OBJECT IDENTIFIER (OID) of a TimeTicks, TimeStamp, or
     DateAndTime object that indicates a discontinuity in the value
     at expObjectID.

     This object is instantiated only if expObjectSampleType is
     'deltaValue' or 'changedValue'.

     The OID may be for a leaf object (e.g. sysUpTime.0) or may
     be wildcarded to match expObjectID.

     This object supports normal checking for a discontinuity in a
     counter.  Note that if this object does not point to sysUpTime
     discontinuity checking must still check sysUpTime for an overall
     discontinuity.

     If the object identified is not accessible no discontinuity
     check will be made.
""")


class _ExpObjectDiscontinuityIDWildcard_Type(TruthValue):
    """Custom type expObjectDiscontinuityIDWildcard based on TruthValue"""


_ExpObjectDiscontinuityIDWildcard_Object = MibTableColumn
expObjectDiscontinuityIDWildcard = _ExpObjectDiscontinuityIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 6),
    _ExpObjectDiscontinuityIDWildcard_Type()
)
expObjectDiscontinuityIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectDiscontinuityIDWildcard.setStatus("current")
if mibBuilder.loadTexts:
    expObjectDiscontinuityIDWildcard.setDescription("""\
A true value indicates the expObjectDeltaDiscontinuityID of
     this row is a wildcard object.  False indicates that
     expObjectDeltaDiscontinuityID is fully instanced.

     This object is instantiated only if expObjectSampleType is
     'deltaValue' or 'changedValue'.

     NOTE:  The simplest implementations of this MIB may not allow
     wildcards.
""")


class _ExpObjectDiscontinuityIDType_Type(Integer32):
    """Custom type expObjectDiscontinuityIDType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dateAndTime", 3),
          ("timeStamp", 2),
          ("timeTicks", 1))
    )


_ExpObjectDiscontinuityIDType_Type.__name__ = "Integer32"
_ExpObjectDiscontinuityIDType_Object = MibTableColumn
expObjectDiscontinuityIDType = _ExpObjectDiscontinuityIDType_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 7),
    _ExpObjectDiscontinuityIDType_Type()
)
expObjectDiscontinuityIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectDiscontinuityIDType.setStatus("current")
if mibBuilder.loadTexts:
    expObjectDiscontinuityIDType.setDescription("""\
The value 'timeTicks' indicates the expObjectDeltaDiscontinuityID
     of this row is of syntax TimeTicks.  The value 'timeStamp' indicates
     syntax TimeStamp.  The value 'dateAndTime indicates syntax
     DateAndTime.

     This object is instantiated only if expObjectSampleType is
     'deltaValue' or 'changedValue'.
""")


class _ExpObjectConditional_Type(ObjectIdentifier):
    """Custom type expObjectConditional based on ObjectIdentifier"""
    defaultValue = "(0, 0)"


_ExpObjectConditional_Object = MibTableColumn
expObjectConditional = _ExpObjectConditional_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 8),
    _ExpObjectConditional_Type()
)
expObjectConditional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectConditional.setStatus("current")
if mibBuilder.loadTexts:
    expObjectConditional.setDescription("""\
The OBJECT IDENTIFIER (OID) of an object that overrides
     whether the instance of expObjectID is to be considered
     usable.  If the value of the object at expObjectConditional
     is 0 or not instantiated, the object at expObjectID is
     treated as if it is not instantiated.  In other words,
     expObjectConditional is a filter that controls whether or
     not to use the value at expObjectID.

     The OID may be for a leaf object (e.g. sysObjectID.0) or may be
     wildcarded to match expObjectID.  If expObject is wildcarded and
     expObjectID in the same row is not, the wild portion of
     expObjectConditional must match the wildcarding of the rest of
     the expression.  If no object in the expression is wildcarded
     but expObjectConditional is, use the lexically first instance
     (if any) of expObjectConditional.

     If the value of expObjectConditional is 0.0 operation is
     as if the value pointed to by expObjectConditional is a
     non-zero (true) value.

     Note that expObjectConditional can not trivially use an object
     of syntax TruthValue, since the underlying value is not 0 or 1.
""")


class _ExpObjectConditionalWildcard_Type(TruthValue):
    """Custom type expObjectConditionalWildcard based on TruthValue"""


_ExpObjectConditionalWildcard_Object = MibTableColumn
expObjectConditionalWildcard = _ExpObjectConditionalWildcard_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 9),
    _ExpObjectConditionalWildcard_Type()
)
expObjectConditionalWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectConditionalWildcard.setStatus("current")
if mibBuilder.loadTexts:
    expObjectConditionalWildcard.setDescription("""\
A true value indicates the expObjectConditional of this row is
     a wildcard object. False indicates that expObjectConditional is
     fully instanced.

     NOTE: The simplest implementations of this MIB may not allow
     wildcards.
""")
_ExpObjectEntryStatus_Type = RowStatus
_ExpObjectEntryStatus_Object = MibTableColumn
expObjectEntryStatus = _ExpObjectEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 2, 3, 1, 10),
    _ExpObjectEntryStatus_Type()
)
expObjectEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    expObjectEntryStatus.setStatus("current")
if mibBuilder.loadTexts:
    expObjectEntryStatus.setDescription("""\
The control that allows creation/deletion of entries.

     Objects in this table may be changed while
     expObjectEntryStatus is in any state.
""")
_ExpValue_ObjectIdentity = ObjectIdentity
expValue = _ExpValue_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 1, 3)
)
_ExpValueTable_Object = MibTable
expValueTable = _ExpValueTable_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1)
)
if mibBuilder.loadTexts:
    expValueTable.setStatus("current")
if mibBuilder.loadTexts:
    expValueTable.setDescription("""\
A table of values from evaluated expressions.
""")
_ExpValueEntry_Object = MibTableRow
expValueEntry = _ExpValueEntry_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1)
)
expValueEntry.setIndexNames(
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionOwner"),
    (0, "DISMAN-EXPRESSION-MIB", "expExpressionName"),
    (1, "DISMAN-EXPRESSION-MIB", "expValueInstance"),
)
if mibBuilder.loadTexts:
    expValueEntry.setStatus("current")
if mibBuilder.loadTexts:
    expValueEntry.setDescription("""\
A single value from an evaluated expression.  For a given
     instance, only one 'Val' object in the conceptual row will be
     instantiated, that is, the one with the appropriate type for
     the value.  For values that contain no objects of
     expObjectSampleType 'deltaValue' or 'changedValue', reading a
     value from the table causes the evaluation of the expression
     for that value.  For those that contain a 'deltaValue' or
     'changedValue' the value read is as of the last sampling
     interval.

     If in the attempt to evaluate the expression one or more
     of the necessary objects is not available, the corresponding
     entry in this table is effectively not instantiated.

     To maintain security of MIB information, when creating a new
     row in this table, the managed system must record the security
     credentials of the requester.  These security credentials are
     the parameters necessary as inputs to isAccessAllowed from
     [RFC2571]. When obtaining the objects that make up the
     expression, the system must (conceptually) use isAccessAllowed to
     ensure that it does not violate security.

     The evaluation of that expression takes place under the

     security credentials of the creator of its expExpressionEntry.

     To maintain security of MIB information, expression evaluation must
     take place using security credentials for the implied Gets of the
     objects in the expression as inputs (conceptually) to
     isAccessAllowed from the Architecture for Describing SNMP
     Management Frameworks.  These are the security credentials of the
     creator of the corresponding expExpressionEntry.
""")
_ExpValueInstance_Type = ObjectIdentifier
_ExpValueInstance_Object = MibTableColumn
expValueInstance = _ExpValueInstance_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 1),
    _ExpValueInstance_Type()
)
expValueInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expValueInstance.setStatus("current")
if mibBuilder.loadTexts:
    expValueInstance.setDescription("""\
The final instance portion of a value's OID according to
     the wildcarding in instances of expObjectID for the
     expression.  The prefix of this OID fragment is 0.0,
     leading to the following behavior.

     If there is no wildcarding, the value is 0.0.0.  In other
     words, there is one value which standing alone would have
     been a scalar with a 0 at the end of its OID.

     If there is wildcarding, the value is 0.0 followed by
     a value that the wildcard can take, thus defining one value
     instance for each real, possible value of the wildcard.
     So, for example, if the wildcard worked out to be an ifIndex,
     there is an expValueInstance for each applicable ifIndex.
""")
_ExpValueCounter32Val_Type = Counter32
_ExpValueCounter32Val_Object = MibTableColumn
expValueCounter32Val = _ExpValueCounter32Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 2),
    _ExpValueCounter32Val_Type()
)
expValueCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueCounter32Val.setStatus("current")
if mibBuilder.loadTexts:
    expValueCounter32Val.setDescription("""\
The value when expExpressionValueType is 'counter32'.
""")
_ExpValueUnsigned32Val_Type = Unsigned32
_ExpValueUnsigned32Val_Object = MibTableColumn
expValueUnsigned32Val = _ExpValueUnsigned32Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 3),
    _ExpValueUnsigned32Val_Type()
)
expValueUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueUnsigned32Val.setStatus("current")
if mibBuilder.loadTexts:
    expValueUnsigned32Val.setDescription("""\
The value when expExpressionValueType is 'unsigned32'.
""")
_ExpValueTimeTicksVal_Type = TimeTicks
_ExpValueTimeTicksVal_Object = MibTableColumn
expValueTimeTicksVal = _ExpValueTimeTicksVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 4),
    _ExpValueTimeTicksVal_Type()
)
expValueTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueTimeTicksVal.setStatus("current")
if mibBuilder.loadTexts:
    expValueTimeTicksVal.setDescription("""\
The value when expExpressionValueType is 'timeTicks'.
""")
_ExpValueInteger32Val_Type = Integer32
_ExpValueInteger32Val_Object = MibTableColumn
expValueInteger32Val = _ExpValueInteger32Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 5),
    _ExpValueInteger32Val_Type()
)
expValueInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueInteger32Val.setStatus("current")
if mibBuilder.loadTexts:
    expValueInteger32Val.setDescription("""\
The value when expExpressionValueType is 'integer32'.
""")
_ExpValueIpAddressVal_Type = IpAddress
_ExpValueIpAddressVal_Object = MibTableColumn
expValueIpAddressVal = _ExpValueIpAddressVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 6),
    _ExpValueIpAddressVal_Type()
)
expValueIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueIpAddressVal.setStatus("current")
if mibBuilder.loadTexts:
    expValueIpAddressVal.setDescription("""\
The value when expExpressionValueType is 'ipAddress'.
""")


class _ExpValueOctetStringVal_Type(OctetString):
    """Custom type expValueOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65536),
    )


_ExpValueOctetStringVal_Type.__name__ = "OctetString"
_ExpValueOctetStringVal_Object = MibTableColumn
expValueOctetStringVal = _ExpValueOctetStringVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 7),
    _ExpValueOctetStringVal_Type()
)
expValueOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueOctetStringVal.setStatus("current")
if mibBuilder.loadTexts:
    expValueOctetStringVal.setDescription("""\
The value when expExpressionValueType is 'octetString'.
""")
_ExpValueOidVal_Type = ObjectIdentifier
_ExpValueOidVal_Object = MibTableColumn
expValueOidVal = _ExpValueOidVal_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 8),
    _ExpValueOidVal_Type()
)
expValueOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueOidVal.setStatus("current")
if mibBuilder.loadTexts:
    expValueOidVal.setDescription("""\
The value when expExpressionValueType is 'objectId'.
""")
_ExpValueCounter64Val_Type = Counter64
_ExpValueCounter64Val_Object = MibTableColumn
expValueCounter64Val = _ExpValueCounter64Val_Object(
    (1, 3, 6, 1, 2, 1, 90, 1, 3, 1, 1, 9),
    _ExpValueCounter64Val_Type()
)
expValueCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expValueCounter64Val.setStatus("current")
if mibBuilder.loadTexts:
    expValueCounter64Val.setDescription("""\
The value when expExpressionValueType is 'counter64'.
""")
_DismanExpressionMIBConformance_ObjectIdentity = ObjectIdentity
dismanExpressionMIBConformance = _DismanExpressionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 3)
)
_DismanExpressionMIBCompliances_ObjectIdentity = ObjectIdentity
dismanExpressionMIBCompliances = _DismanExpressionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 3, 1)
)
_DismanExpressionMIBGroups_ObjectIdentity = ObjectIdentity
dismanExpressionMIBGroups = _DismanExpressionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 90, 3, 2)
)

# Managed Objects groups

dismanExpressionResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 90, 3, 2, 1)
)
dismanExpressionResourceGroup.setObjects(
      *(("DISMAN-EXPRESSION-MIB", "expResourceDeltaMinimum"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstanceMaximum"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstances"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstancesHigh"),
        ("DISMAN-EXPRESSION-MIB", "expResourceDeltaWildcardInstanceResourceLacks"))
)
if mibBuilder.loadTexts:
    dismanExpressionResourceGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanExpressionResourceGroup.setDescription("""\
Expression definition resource management.
""")

dismanExpressionDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 90, 3, 2, 2)
)
dismanExpressionDefinitionGroup.setObjects(
      *(("DISMAN-EXPRESSION-MIB", "expExpression"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionValueType"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionComment"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionDeltaInterval"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionPrefix"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionErrors"),
        ("DISMAN-EXPRESSION-MIB", "expExpressionEntryStatus"),
        ("DISMAN-EXPRESSION-MIB", "expErrorTime"),
        ("DISMAN-EXPRESSION-MIB", "expErrorIndex"),
        ("DISMAN-EXPRESSION-MIB", "expErrorCode"),
        ("DISMAN-EXPRESSION-MIB", "expErrorInstance"),
        ("DISMAN-EXPRESSION-MIB", "expObjectID"),
        ("DISMAN-EXPRESSION-MIB", "expObjectIDWildcard"),
        ("DISMAN-EXPRESSION-MIB", "expObjectSampleType"),
        ("DISMAN-EXPRESSION-MIB", "expObjectDeltaDiscontinuityID"),
        ("DISMAN-EXPRESSION-MIB", "expObjectDiscontinuityIDWildcard"),
        ("DISMAN-EXPRESSION-MIB", "expObjectDiscontinuityIDType"),
        ("DISMAN-EXPRESSION-MIB", "expObjectConditional"),
        ("DISMAN-EXPRESSION-MIB", "expObjectConditionalWildcard"),
        ("DISMAN-EXPRESSION-MIB", "expObjectEntryStatus"))
)
if mibBuilder.loadTexts:
    dismanExpressionDefinitionGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanExpressionDefinitionGroup.setDescription("""\
Expression definition.
""")

dismanExpressionValueGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 90, 3, 2, 3)
)
dismanExpressionValueGroup.setObjects(
      *(("DISMAN-EXPRESSION-MIB", "expValueCounter32Val"),
        ("DISMAN-EXPRESSION-MIB", "expValueUnsigned32Val"),
        ("DISMAN-EXPRESSION-MIB", "expValueTimeTicksVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueInteger32Val"),
        ("DISMAN-EXPRESSION-MIB", "expValueIpAddressVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueOctetStringVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueOidVal"),
        ("DISMAN-EXPRESSION-MIB", "expValueCounter64Val"))
)
if mibBuilder.loadTexts:
    dismanExpressionValueGroup.setStatus("current")
if mibBuilder.loadTexts:
    dismanExpressionValueGroup.setDescription("""\
Expression value.
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dismanExpressionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 90, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dismanExpressionMIBCompliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    dismanExpressionMIBCompliance.setDescription("""\
The compliance statement for entities which implement
          the Expression MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-EXPRESSION-MIB",
    **{"sysUpTimeInstance": sysUpTimeInstance,
       "dismanExpressionMIB": dismanExpressionMIB,
       "dismanExpressionMIBObjects": dismanExpressionMIBObjects,
       "expResource": expResource,
       "expResourceDeltaMinimum": expResourceDeltaMinimum,
       "expResourceDeltaWildcardInstanceMaximum": expResourceDeltaWildcardInstanceMaximum,
       "expResourceDeltaWildcardInstances": expResourceDeltaWildcardInstances,
       "expResourceDeltaWildcardInstancesHigh": expResourceDeltaWildcardInstancesHigh,
       "expResourceDeltaWildcardInstanceResourceLacks": expResourceDeltaWildcardInstanceResourceLacks,
       "expDefine": expDefine,
       "expExpressionTable": expExpressionTable,
       "expExpressionEntry": expExpressionEntry,
       "expExpressionOwner": expExpressionOwner,
       "expExpressionName": expExpressionName,
       "expExpression": expExpression,
       "expExpressionValueType": expExpressionValueType,
       "expExpressionComment": expExpressionComment,
       "expExpressionDeltaInterval": expExpressionDeltaInterval,
       "expExpressionPrefix": expExpressionPrefix,
       "expExpressionErrors": expExpressionErrors,
       "expExpressionEntryStatus": expExpressionEntryStatus,
       "expErrorTable": expErrorTable,
       "expErrorEntry": expErrorEntry,
       "expErrorTime": expErrorTime,
       "expErrorIndex": expErrorIndex,
       "expErrorCode": expErrorCode,
       "expErrorInstance": expErrorInstance,
       "expObjectTable": expObjectTable,
       "expObjectEntry": expObjectEntry,
       "expObjectIndex": expObjectIndex,
       "expObjectID": expObjectID,
       "expObjectIDWildcard": expObjectIDWildcard,
       "expObjectSampleType": expObjectSampleType,
       "expObjectDeltaDiscontinuityID": expObjectDeltaDiscontinuityID,
       "expObjectDiscontinuityIDWildcard": expObjectDiscontinuityIDWildcard,
       "expObjectDiscontinuityIDType": expObjectDiscontinuityIDType,
       "expObjectConditional": expObjectConditional,
       "expObjectConditionalWildcard": expObjectConditionalWildcard,
       "expObjectEntryStatus": expObjectEntryStatus,
       "expValue": expValue,
       "expValueTable": expValueTable,
       "expValueEntry": expValueEntry,
       "expValueInstance": expValueInstance,
       "expValueCounter32Val": expValueCounter32Val,
       "expValueUnsigned32Val": expValueUnsigned32Val,
       "expValueTimeTicksVal": expValueTimeTicksVal,
       "expValueInteger32Val": expValueInteger32Val,
       "expValueIpAddressVal": expValueIpAddressVal,
       "expValueOctetStringVal": expValueOctetStringVal,
       "expValueOidVal": expValueOidVal,
       "expValueCounter64Val": expValueCounter64Val,
       "dismanExpressionMIBConformance": dismanExpressionMIBConformance,
       "dismanExpressionMIBCompliances": dismanExpressionMIBCompliances,
       "dismanExpressionMIBCompliance": dismanExpressionMIBCompliance,
       "dismanExpressionMIBGroups": dismanExpressionMIBGroups,
       "dismanExpressionResourceGroup": dismanExpressionResourceGroup,
       "dismanExpressionDefinitionGroup": dismanExpressionDefinitionGroup,
       "dismanExpressionValueGroup": dismanExpressionValueGroup}
)
