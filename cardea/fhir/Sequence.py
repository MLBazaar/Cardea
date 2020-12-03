from .fhirbase import fhirbase


class Sequence(fhirbase):
    """
    Raw data describing a biological sequence.

    Args:
        resourceType: This is a Sequence resource
        identifier: A unique identifier for this particular sequence instance.
            This is a FHIR-defined id.
        type: Amino Acid Sequence/ DNA Sequence / RNA Sequence.
        coordinateSystem: Whether the sequence is numbered starting at 0
            (0-based numbering or coordinates, inclusive start, exclusive end) or
            starting at 1 (1-based numbering, inclusive start and inclusive end).
        patient: The patient whose sequencing results are described by this
            resource.
        specimen: Specimen used for sequencing.
        device: The method for sequencing, for example, chip information.
        performer: The organization or lab that should be responsible for this
            result.
        quantity: The number of copies of the seqeunce of interest. (RNASeq).
        referenceSeq: A sequence that is used as a reference to describe
            variants that are present in a sequence analyzed.
        variant: The definition of variant here originates from Sequence
            ontology
            ([variant_of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
            This element can represent amino acid or nucleic sequence
            change(including insertion,deletion,SNP,etc.)  It can represent some
            complex mutation or segment variation with the assist of CIGAR string.
        observedSeq: Sequence that was observed. It is the result marked by
            referenceSeq along with variant records on referenceSeq. This shall
            starts from referenceSeq.windowStart and end by
            referenceSeq.windowEnd.
        quality: An experimental feature attribute that defines the quality of
            the feature in a quantitative way, such as a phred quality score
            ([SO:0001686](http://www.sequenceontology.org/browser/current_svn/term/SO:0001686)).
        readCoverage: Coverage (read depth or depth) is the average number of
            reads representing a given nucleotide in the reconstructed sequence.
        repository: Configurations of the external repository. The repository
            shall store target's observedSeq or records related with target's
            observedSeq.
        pointer: Pointer to next atomic sequence which at most contains one
            variant.
    """

    __name__ = 'Sequence'

    def __init__(self, dict_values=None):
        self.resourceType = 'Sequence'
        # type: str
        # possible values: Sequence

        self.type = None
        # type: str
        # possible values: aa, dna, rna

        self.coordinateSystem = None
        # type: int

        self.patient = None
        # reference to Reference: identifier

        self.specimen = None
        # reference to Reference: identifier

        self.device = None
        # reference to Reference: identifier

        self.performer = None
        # reference to Reference: identifier

        self.quantity = None
        # reference to Quantity

        self.referenceSeq = None
        # reference to Sequence_ReferenceSeq

        self.variant = None
        # type: list
        # reference to Sequence_Variant

        self.observedSeq = None
        # type: str

        self.quality = None
        # type: list
        # reference to Sequence_Quality

        self.readCoverage = None
        # type: int

        self.repository = None
        # type: list
        # reference to Sequence_Repository

        self.pointer = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'aa', 'dna', 'rna']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'aa, dna, rna'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'pointer'},

            {'parent_entity': 'Sequence_Quality',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'quality'},

            {'parent_entity': 'Sequence_Repository',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'repository'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'specimen'},

            {'parent_entity': 'Sequence_ReferenceSeq',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'referenceSeq'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'performer'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'identifier'},

            {'parent_entity': 'Sequence_Variant',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'variant'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'device'},
        ]


class Sequence_ReferenceSeq(fhirbase):
    """
    Raw data describing a biological sequence.

    Args:
        chromosome: Structural unit composed of a nucleic acid molecule which
            controls its own replication through the interaction of specific
            proteins at one or more origins of replication
            ([SO:0000340](http://www.sequenceontology.org/browser/current_svn/term/SO:0000340)).
        genomeBuild: The Genome Build used for reference, following GRCh build
            versions e.g. 'GRCh 37'.  Version number must be included if a
            versioned release of a primary build was used.
        referenceSeqId: Reference identifier of reference sequence submitted
            to NCBI. It must match the type in the Sequence.type field. For
            example, the prefix, *NG_* identifies reference sequence for genes,
            *NM_* for messenger RNA transcripts, and *NP_* for amino acid
            sequences.
        referenceSeqPointer: A Pointer to another Sequence entity as reference
            sequence.
        referenceSeqString: A string like "ACGT".
        strand: Directionality of DNA sequence. Available values are "1" for
            the plus strand (5' to 3')/Watson/Sense/positive  and "-1" for the
            minus strand(3' to 5')/Crick/Antisense/negative.
        windowStart: Start position of the window on the reference sequence.
            If the coordinate system is either 0-based or 1-based, then start
            position is inclusive.
        windowEnd: End position of the window on the reference sequence. If
            the coordinate system is 0-based then end is is exclusive and does not
            include the last position. If the coordinate system is 1-base, then
            end is inclusive and includes the last position.
    """

    __name__ = 'Sequence_ReferenceSeq'

    def __init__(self, dict_values=None):
        self.chromosome = None
        # reference to CodeableConcept

        self.genomeBuild = None
        # type: str

        self.referenceSeqId = None
        # reference to CodeableConcept

        self.referenceSeqPointer = None
        # reference to Reference: identifier

        self.referenceSeqString = None
        # type: str

        self.strand = None
        # type: int

        self.windowStart = None
        # type: int

        self.windowEnd = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_ReferenceSeq',
             'child_variable': 'chromosome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_ReferenceSeq',
             'child_variable': 'referenceSeqId'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence_ReferenceSeq',
             'child_variable': 'referenceSeqPointer'},
        ]


class Sequence_Variant(fhirbase):
    """
    Raw data describing a biological sequence.

    Args:
        start: Start position of the variant on the  reference sequence.If the
            coordinate system is either 0-based or 1-based, then start position is
            inclusive.
        end: End position of the variant on the reference sequence.If the
            coordinate system is 0-based then end is is exclusive and does not
            include the last position. If the coordinate system is 1-base, then
            end is inclusive and includes the last position.
        observedAllele: An allele is one of a set of coexisting sequence
            variants of a gene
            ([SO:0001023](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
            Nucleotide(s)/amino acids from start position of sequence to stop
            position of sequence on the positive (+) strand of the observed
            sequence. When the sequence  type is DNA, it should be the sequence on
            the positive (+) strand. This will lay in the range between
            variant.start and variant.end.
        referenceAllele: An allele is one of a set of coexisting sequence
            variants of a gene
            ([SO:0001023](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
            Nucleotide(s)/amino acids from start position of sequence to stop
            position of sequence on the positive (+) strand of the reference
            sequence. When the sequence  type is DNA, it should be the sequence on
            the positive (+) strand. This will lay in the range between
            variant.start and variant.end.
        cigar: Extended CIGAR string for aligning the sequence with reference
            bases. See detailed documentation
            [here](http://support.illumina.com/help/SequencingAnalysisWorkflow/Content/Vault/Informatics/Sequencing_Analysis/CASAVA/swSEQ_mCA_ExtendedCIGARFormat.htm).
        variantPointer: A pointer to an Observation containing variant
            information.
    """

    __name__ = 'Sequence_Variant'

    def __init__(self, dict_values=None):
        self.start = None
        # type: int

        self.end = None
        # type: int

        self.observedAllele = None
        # type: str

        self.referenceAllele = None
        # type: str

        self.cigar = None
        # type: str

        self.variantPointer = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence_Variant',
             'child_variable': 'variantPointer'},
        ]


class Sequence_Quality(fhirbase):
    """
    Raw data describing a biological sequence.

    Args:
        type: INDEL / SNP / Undefined variant.
        standardSequence: Gold standard sequence used for comparing against.
        start: Start position of the sequence. If the coordinate system is
            either 0-based or 1-based, then start position is inclusive.
        end: End position of the sequence.If the coordinate system is 0-based
            then end is is exclusive and does not include the last position. If
            the coordinate system is 1-base, then end is inclusive and includes
            the last position.
        score: The score of an experimentally derived feature such as a
            p-value
            ([SO:0001685](http://www.sequenceontology.org/browser/current_svn/term/SO:0001685)).
        method: Which method is used to get sequence quality.
        truthTP: True positives, from the perspective of the truth data, i.e.
            the number of sites in the Truth Call Set for which there are paths
            through the Query Call Set that are consistent with all of the alleles
            at this site, and for which there is an accurate genotype call for the
            event.
        queryTP: True positives, from the perspective of the query data, i.e.
            the number of sites in the Query Call Set for which there are paths
            through the Truth Call Set that are consistent with all of the alleles
            at this site, and for which there is an accurate genotype call for the
            event.
        truthFN: False negatives, i.e. the number of sites in the Truth Call
            Set for which there is no path through the Query Call Set that is
            consistent with all of the alleles at this site, or sites for which
            there is an inaccurate genotype call for the event. Sites with correct
            variant but incorrect genotype are counted here.
        queryFP: False positives, i.e. the number of sites in the Query Call
            Set for which there is no path through the Truth Call Set that is
            consistent with this site. Sites with correct variant but incorrect
            genotype are counted here.
        gtFP: The number of false positives where the non-REF alleles in the
            Truth and Query Call Sets match (i.e. cases where the truth is 1/1 and
            the query is 0/1 or similar).
        precision: QUERY.TP / (QUERY.TP + QUERY.FP).
        recall: TRUTH.TP / (TRUTH.TP + TRUTH.FN).
        fScore: Harmonic mean of Recall and Precision, computed as: 2 *
            precision * recall / (precision + recall).
    """

    __name__ = 'Sequence_Quality'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: indel, snp, unknown

        self.standardSequence = None
        # reference to CodeableConcept

        self.start = None
        # type: int

        self.end = None
        # type: int

        self.score = None
        # reference to Quantity

        self.method = None
        # reference to CodeableConcept

        self.truthTP = None
        # type: int

        self.queryTP = None
        # type: int

        self.truthFN = None
        # type: int

        self.queryFP = None
        # type: int

        self.gtFP = None
        # type: int

        self.precision = None
        # type: int

        self.recall = None
        # type: int

        self.fScore = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'indel', 'snp', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'indel, snp, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_Quality',
             'child_variable': 'method'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_Quality',
             'child_variable': 'score'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_Quality',
             'child_variable': 'standardSequence'},
        ]


class Sequence_Repository(fhirbase):
    """
    Raw data describing a biological sequence.

    Args:
        type: Click and see / RESTful API / Need login to see / RESTful API
            with authentication / Other ways to see resource.
        url: URI of an external repository which contains further details
            about the genetics data.
        name: URI of an external repository which contains further details
            about the genetics data.
        datasetId: Id of the variant in this external repository. The server
            will understand how to use this id to call for more info about
            datasets in external repository.
        variantsetId: Id of the variantset in this external repository. The
            server will understand how to use this id to call for more info about
            variantsets in external repository.
        readsetId: Id of the read in this external repository.
    """

    __name__ = 'Sequence_Repository'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: directlink, openapi, login, oauth, other

        self.url = None
        # type: str

        self.name = None
        # type: str

        self.datasetId = None
        # type: str

        self.variantsetId = None
        # type: str

        self.readsetId = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'directlink', 'openapi', 'login', 'oauth', 'other']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'directlink, openapi, login, oauth, other'))
