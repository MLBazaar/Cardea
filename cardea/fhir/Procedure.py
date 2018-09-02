from .fhirbase import fhirbase


class Procedure(fhirbase):
    """An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    def __init__(self, dict_values=None):
        # this is a procedure resource
        self.resourceType = 'Procedure'
        # type = string
        # possible values: Procedure

        # a protocol, guideline, orderset or other definition that was adhered to
        # in whole or in part by this procedure.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # a reference to a resource that contains details of the request for this
        # procedure.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # a larger event of which this particular procedure is a component or
        # step.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # a code specifying the state of the procedure. generally this will be in-
        # progress or completed state.
        self.status = None
        # type = string

        # set this to true if the record is saying that the procedure was not
        # performed.
        self.notDone = None
        # type = boolean

        # a code indicating why the procedure was not performed.
        self.notDoneReason = None
        # reference to CodeableConcept: CodeableConcept

        # a code that classifies the procedure for searching, sorting and display
        # purposes (e.g. "surgical procedure").
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # the specific procedure that is performed. use text if the exact nature
        # of the procedure cannot be coded (e.g. "laparoscopic appendectomy").
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the person, animal or group on which the procedure was performed.
        self.subject = None
        # reference to Reference: identifier

        # the encounter during which the procedure was performed.
        self.context = None
        # reference to Reference: identifier

        # the date(time)/period over which the procedure was performed. allows a
        # period to support complex procedures that span more than one date, and
        # also allows for the length of the procedure to be captured.
        self.performedDateTime = None
        # type = string

        # the date(time)/period over which the procedure was performed. allows a
        # period to support complex procedures that span more than one date, and
        # also allows for the length of the procedure to be captured.
        self.performedPeriod = None
        # reference to Period: Period

        # limited to 'real' people rather than equipment.
        self.performer = None
        # type = array
        # reference to Procedure_Performer: Procedure_Performer

        # the location where the procedure actually happened.  e.g. a newborn at
        # home, a tracheostomy at a restaurant.
        self.location = None
        # reference to Reference: identifier

        # the coded reason why the procedure was performed. this may be coded
        # entity of some type, or may simply be present as text.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the condition that is the reason why the procedure was performed.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # detailed and structured anatomical location information. multiple
        # locations are allowed - e.g. multiple punch biopsies of a lesion.
        self.bodySite = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the outcome of the procedure - did it resolve reasons for the procedure
        # being performed?
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # this could be a histology result, pathology report, surgical report,
        # etc..
        self.report = None
        # type = array
        # reference to Reference: identifier

        # any complications that occurred during the procedure, or in the
        # immediate post-performance period. these are generally tracked
        # separately from the notes, which will typically describe the procedure
        # itself rather than any 'post procedure' issues.
        self.complication = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # any complications that occurred during the procedure, or in the
        # immediate post-performance period.
        self.complicationDetail = None
        # type = array
        # reference to Reference: identifier

        # if the procedure required specific follow up - e.g. removal of sutures.
        # the followup may be represented as a simple note, or could potentially
        # be more complex in which case the careplan resource can be used.
        self.followUp = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # any other notes about the procedure.  e.g. the operative notes.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # a device that is implanted, removed or otherwise manipulated
        # (calibration, battery replacement, fitting a prosthesis, attaching a
        # wound-vac, etc.) as a focal portion of the procedure.
        self.focalDevice = None
        # type = array
        # reference to Procedure_FocalDevice: Procedure_FocalDevice

        # identifies medications, devices and any other substance used as part of
        # the procedure.
        self.usedReference = None
        # type = array
        # reference to Reference: identifier

        # identifies coded items that were used as part of the procedure.
        self.usedCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # this records identifiers associated with this procedure that are defined
        # by business processes and/or used to refer to it when a direct url
        # reference to the resource itself is not appropriate (e.g. in cda
        # documents, or in written / printed documentation).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'usedReference'},

            {'parent_entity': 'Procedure_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'performer'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'performedPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'outcome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'category'},

            {'parent_entity': 'Procedure_FocalDevice',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'focalDevice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'followUp'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'report'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'complication'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'notDoneReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'complicationDetail'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'definition'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'usedCode'},
        ]


class Procedure_Performer(fhirbase):
    """An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    def __init__(self, dict_values=None):
        # for example: surgeon, anaethetist, endoscopist.
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the practitioner who was involved in the procedure.
        self.actor = None
        # reference to Reference: identifier

        # the organization the device or practitioner was acting on behalf of.
        self.onBehalfOf = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure_Performer',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure_Performer',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure_Performer',
             'child_variable': 'role'},
        ]


class Procedure_FocalDevice(fhirbase):
    """An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """

    def __init__(self, dict_values=None):
        # the kind of change that happened to the device during the procedure.
        self.action = None
        # reference to CodeableConcept: CodeableConcept

        # the device that was manipulated (changed) during the procedure.
        self.manipulated = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure_FocalDevice',
             'child_variable': 'action'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure_FocalDevice',
             'child_variable': 'manipulated'},
        ]
