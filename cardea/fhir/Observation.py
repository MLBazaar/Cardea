from .fhirbase import fhirbase


class Observation(fhirbase):
    """Measurements and simple assertions made about a patient, device or other
    subject.
    """

    def __init__(self, dict_values=None):
        # this is a observation resource
        self.resourceType = 'Observation'
        # type = string
        # possible values: Observation

        # a plan, proposal or order that is fulfilled in whole or in part by this
        # event.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # the status of the result value.
        self.status = None
        # type = string
        # possible values: registered, preliminary, final, amended,
        # corrected, cancelled, entered-in-error, unknown

        # a code that classifies the general type of observation being made.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # describes what was observed. sometimes this is called the observation
        # "name".
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the patient, or group of patients, location, or device whose
        # characteristics (direct or indirect) are described by the observation
        # and into whose record the observation is placed.  comments: indirect
        # characteristics may be those of a specimen, fetus, donor,  other
        # observer (for example a relative or emt), or any observation made about
        # the subject.
        self.subject = None
        # reference to Reference: identifier

        # the healthcare event  (e.g. a patient and healthcare provider
        # interaction) during which this observation is made.
        self.context = None
        # reference to Reference: identifier

        # the time or time-period the observed value is asserted as being true.
        # for biological subjects - e.g. human patients - this is usually called
        # the "physiologically relevant time". this is usually either the time of
        # the procedure or of specimen collection, but very often the source of
        # the date/time is not known, only the date/time itself.
        self.effectiveDateTime = None
        # type = string

        # the time or time-period the observed value is asserted as being true.
        # for biological subjects - e.g. human patients - this is usually called
        # the "physiologically relevant time". this is usually either the time of
        # the procedure or of specimen collection, but very often the source of
        # the date/time is not known, only the date/time itself.
        self.effectivePeriod = None
        # reference to Period: Period

        # the date and time this observation was made available to providers,
        # typically after the results have been reviewed and verified.
        self.issued = None
        # type = string

        # who was responsible for asserting the observed value as "true".
        self.performer = None
        # type = array
        # reference to Reference: identifier

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueString = None
        # type = string

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueBoolean = None
        # type = boolean

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueRange = None
        # reference to Range: Range

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueRatio = None
        # reference to Ratio: Ratio

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueSampledData = None
        # reference to SampledData: SampledData

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueTime = None
        # type = string

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueDateTime = None
        # type = string

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valuePeriod = None
        # reference to Period: Period

        # provides a reason why the expected value in the element
        # observation.value[x] is missing.
        self.dataAbsentReason = None
        # reference to CodeableConcept: CodeableConcept

        # the assessment made based on the result of the observation.  intended as
        # a simple compact code often placed adjacent to the result value in
        # reports and flow sheets to signal the meaning/normalcy status of the
        # result. otherwise known as abnormal flag.
        self.interpretation = None
        # reference to CodeableConcept: CodeableConcept

        # may include statements about significant, unexpected or unreliable
        # values, or information about the source of the value where this may be
        # relevant to the interpretation of the result.
        self.comment = None
        # type = string

        # indicates the site on the subject's body where the observation was made
        # (i.e. the target site).
        self.bodySite = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the mechanism used to perform the observation.
        self.method = None
        # reference to CodeableConcept: CodeableConcept

        # the specimen that was used when this observation was made.
        self.specimen = None
        # reference to Reference: identifier

        # the device used to generate the observation data.
        self.device = None
        # reference to Reference: identifier

        # guidance on how to interpret the value by comparison to a normal or
        # recommended range.
        self.referenceRange = None
        # type = array
        # reference to Observation_ReferenceRange: Observation_ReferenceRange

        # a  reference to another resource (usually another observation) whose
        # relationship is defined by the relationship type code.
        self.related = None
        # type = array
        # reference to Observation_Related: Observation_Related

        # some observations have multiple component observations.  these component
        # observations are expressed as separate code value pairs that share the
        # same attributes.  examples include systolic and diastolic component
        # observations for blood pressure measurement and multiple component
        # observations for genetics observations.
        self.component = None
        # type = array
        # reference to Observation_Component: Observation_Component

        # a unique identifier assigned to this observation.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'registered', 'preliminary', 'final', 'amended', 'corrected',
                        'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'registered, preliminary, final, amended, corrected,'
                        'cancelled, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Observation_Component',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'component'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'bodySite'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'interpretation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'dataAbsentReason'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'performer'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'method'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'subject'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'category'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueRange'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'specimen'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'device'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Observation_Related',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'related'},

            {'parent_entity': 'Observation_ReferenceRange',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'referenceRange'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'context'},
        ]


class Observation_ReferenceRange(fhirbase):
    """Measurements and simple assertions made about a patient, device or other
    subject.
    """

    def __init__(self, dict_values=None):
        # the value of the low bound of the reference range.  the low bound of the
        # reference range endpoint is inclusive of the value (e.g.  reference
        # range is >=5 - <=9).   if the low bound is omitted,  it is assumed to be
        # meaningless (e.g. reference range is <=2.3).
        self.low = None
        # reference to Quantity: Quantity

        # the value of the high bound of the reference range.  the high bound of
        # the reference range endpoint is inclusive of the value (e.g.  reference
        # range is >=5 - <=9).   if the high bound is omitted,  it is assumed to
        # be meaningless (e.g. reference range is >= 2.3).
        self.high = None
        # reference to Quantity: Quantity

        # codes to indicate the what part of the targeted reference population it
        # applies to. for example, the normal or therapeutic range.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # codes to indicate the target population this reference range applies to.
        # for example, a reference range may be based on the normal population or
        # a particular sex or race.
        self.appliesTo = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the age at which this reference range is applicable. this is a neonatal
        # age (e.g. number of weeks at term) if the meaning says so.
        self.age = None
        # reference to Range: Range

        # text based reference range in an observation which may be used when a
        # quantitative range is not appropriate for an observation.  an example
        # would be a reference value of "negative" or a list or table of
        # 'normals'.
        self.text = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'type'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'low'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'age'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'appliesTo'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'high'},
        ]


class Observation_Related(fhirbase):
    """Measurements and simple assertions made about a patient, device or other
    subject.
    """

    def __init__(self, dict_values=None):
        # a code specifying the kind of relationship that exists with the target
        # resource.
        self.type = None
        # type = string
        # possible values: has-member, derived-from, sequel-to,
        # replaces, qualified-by, interfered-by

        # a reference to the observation or [[[questionnaireresponse]]] resource
        # that is related to this observation.
        self.target = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'has-member', 'derived-from', 'sequel-to', 'replaces', 'qualified-by',
                        'interfered-by']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'has-member, derived-from, sequel-to, replaces,'
                        'qualified-by, interfered-by'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation_Related',
             'child_variable': 'target'},
        ]


class Observation_Component(fhirbase):
    """Measurements and simple assertions made about a patient, device or other
    subject.
    """

    def __init__(self, dict_values=None):
        # describes what was observed. sometimes this is called the observation
        # "code".
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueString = None
        # type = string

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueRange = None
        # reference to Range: Range

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueRatio = None
        # reference to Ratio: Ratio

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueSampledData = None
        # reference to SampledData: SampledData

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueTime = None
        # type = string

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valueDateTime = None
        # type = string

        # the information determined as a result of making the observation, if the
        # information has a simple value.
        self.valuePeriod = None
        # reference to Period: Period

        # provides a reason why the expected value in the element
        # observation.value[x] is missing.
        self.dataAbsentReason = None
        # reference to CodeableConcept: CodeableConcept

        # the assessment made based on the result of the observation.  intended as
        # a simple compact code often placed adjacent to the result value in
        # reports and flow sheets to signal the meaning/normalcy status of the
        # result. otherwise known as abnormal flag.
        self.interpretation = None
        # reference to CodeableConcept: CodeableConcept

        # guidance on how to interpret the value by comparison to a normal or
        # recommended range.
        self.referenceRange = None
        # type = array
        # reference to Observation_ReferenceRange: Observation_ReferenceRange

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'dataAbsentReason'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'code'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'interpretation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'Observation_ReferenceRange',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'referenceRange'},
        ]
