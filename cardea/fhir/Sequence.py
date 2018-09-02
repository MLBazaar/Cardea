from .fhirbase import fhirbase


class Sequence(fhirbase):
    """Raw data describing a biological sequence.
    """

    def __init__(self, dict_values=None):
        # this is a sequence resource
        self.resourceType = 'Sequence'
        # type = string
        # possible values: Sequence

        # amino acid sequence/ dna sequence / rna sequence.
        self.type = None
        # type = string
        # possible values: aa, dna, rna

        # whether the sequence is numbered starting at 0 (0-based numbering or
        # coordinates, inclusive start, exclusive end) or starting at 1 (1-based
        # numbering, inclusive start and inclusive end).
        self.coordinateSystem = None
        # type = int

        # the patient whose sequencing results are described by this resource.
        self.patient = None
        # reference to Reference: identifier

        # specimen used for sequencing.
        self.specimen = None
        # reference to Reference: identifier

        # the method for sequencing, for example, chip information.
        self.device = None
        # reference to Reference: identifier

        # the organization or lab that should be responsible for this result.
        self.performer = None
        # reference to Reference: identifier

        # the number of copies of the seqeunce of interest. (rnaseq).
        self.quantity = None
        # reference to Quantity: Quantity

        # a sequence that is used as a reference to describe variants that are
        # present in a sequence analyzed.
        self.referenceSeq = None
        # reference to Sequence_ReferenceSeq: Sequence_ReferenceSeq

        # the definition of variant here originates from sequence ontology
        # ([variant_of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
        # this element can represent amino acid or nucleic sequence
        # change(including insertion,deletion,snp,etc.)  it can represent some
        # complex mutation or segment variation with the assist of cigar string.
        self.variant = None
        # type = array
        # reference to Sequence_Variant: Sequence_Variant

        # sequence that was observed. it is the result marked by referenceseq
        # along with variant records on referenceseq. this shall starts from
        # referenceseq.windowstart and end by referenceseq.windowend.
        self.observedSeq = None
        # type = string

        # an experimental feature attribute that defines the quality of the
        # feature in a quantitative way, such as a phred quality score
        # ([so:0001686](http://www.sequenceontology.org/browser/current_svn/term/so:0001686)).
        self.quality = None
        # type = array
        # reference to Sequence_Quality: Sequence_Quality

        # coverage (read depth or depth) is the average number of reads
        # representing a given nucleotide in the reconstructed sequence.
        self.readCoverage = None
        # type = int

        # configurations of the external repository. the repository shall store
        # target's observedseq or records related with target's observedseq.
        self.repository = None
        # type = array
        # reference to Sequence_Repository: Sequence_Repository

        # pointer to next atomic sequence which at most contains one variant.
        self.pointer = None
        # type = array
        # reference to Reference: identifier

        # a unique identifier for this particular sequence instance. this is a
        # fhir-defined id.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'pointer'},

            {'parent_entity': 'Sequence_ReferenceSeq',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'referenceSeq'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'device'},

            {'parent_entity': 'Sequence_Quality',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'quality'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'quantity'},

            {'parent_entity': 'Sequence_Variant',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'variant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'specimen'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence',
             'child_variable': 'patient'},

            {'parent_entity': 'Sequence_Repository',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence',
             'child_variable': 'repository'},
        ]


class Sequence_ReferenceSeq(fhirbase):
    """Raw data describing a biological sequence.
    """

    def __init__(self, dict_values=None):
        # structural unit composed of a nucleic acid molecule which controls its
        # own replication through the interaction of specific proteins at one or
        # more origins of replication
        # ([so:0000340](http://www.sequenceontology.org/browser/current_svn/term/so:0000340)).
        self.chromosome = None
        # reference to CodeableConcept: CodeableConcept

        # the genome build used for reference, following grch build versions e.g.
        # 'grch 37'.  version number must be included if a versioned release of a
        # primary build was used.
        self.genomeBuild = None
        # type = string

        # reference identifier of reference sequence submitted to ncbi. it must
        # match the type in the sequence.type field. for example, the prefix,
        # “ng_” identifies reference sequence for genes, “nm_” for messenger rna
        # transcripts, and “np_” for amino acid sequences.
        self.referenceSeqId = None
        # reference to CodeableConcept: CodeableConcept

        # a pointer to another sequence entity as reference sequence.
        self.referenceSeqPointer = None
        # reference to Reference: identifier

        # a string like "acgt".
        self.referenceSeqString = None
        # type = string

        # directionality of dna sequence. available values are "1" for the plus
        # strand (5' to 3')/watson/sense/positive  and "-1" for the minus
        # strand(3' to 5')/crick/antisense/negative.
        self.strand = None
        # type = int

        # start position of the window on the reference sequence. if the
        # coordinate system is either 0-based or 1-based, then start position is
        # inclusive.
        self.windowStart = None
        # type = int

        # end position of the window on the reference sequence. if the coordinate
        # system is 0-based then end is is exclusive and does not include the last
        # position. if the coordinate system is 1-base, then end is inclusive and
        # includes the last position.
        self.windowEnd = None
        # type = int

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Sequence_ReferenceSeq',
             'child_variable': 'referenceSeqPointer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_ReferenceSeq',
             'child_variable': 'chromosome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_ReferenceSeq',
             'child_variable': 'referenceSeqId'},
        ]


class Sequence_Variant(fhirbase):
    """Raw data describing a biological sequence.
    """

    def __init__(self, dict_values=None):
        # start position of the variant on the  reference sequence.if the
        # coordinate system is either 0-based or 1-based, then start position is
        # inclusive.
        self.start = None
        # type = int

        # end position of the variant on the reference sequence.if the coordinate
        # system is 0-based then end is is exclusive and does not include the last
        # position. if the coordinate system is 1-base, then end is inclusive and
        # includes the last position.
        self.end = None
        # type = int

        # an allele is one of a set of coexisting sequence variants of a gene
        # ([so:0001023](http://www.sequenceontology.org/browser/current_svn/term/so:0001023)).
        # nucleotide(s)/amino acids from start position of sequence to stop
        # position of sequence on the positive (+) strand of the observed
        # sequence. when the sequence  type is dna, it should be the sequence on
        # the positive (+) strand. this will lay in the range between
        # variant.start and variant.end.
        self.observedAllele = None
        # type = string

        # an allele is one of a set of coexisting sequence variants of a gene
        # ([so:0001023](http://www.sequenceontology.org/browser/current_svn/term/so:0001023)).
        # nucleotide(s)/amino acids from start position of sequence to stop
        # position of sequence on the positive (+) strand of the reference
        # sequence. when the sequence  type is dna, it should be the sequence on
        # the positive (+) strand. this will lay in the range between
        # variant.start and variant.end.
        self.referenceAllele = None
        # type = string

        # extended cigar string for aligning the sequence with reference bases.
        # see detailed documentation
        # [here](http://support.illumina.com/help/sequencinganalysisworkflow/content/vault/informatics/sequencing_analysis/casava/swseq_mca_extendedcigarformat.htm).
        self.cigar = None
        # type = string

        # a pointer to an observation containing variant information.
        self.variantPointer = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
    """Raw data describing a biological sequence.
    """

    def __init__(self, dict_values=None):
        # indel / snp / undefined variant.
        self.type = None
        # type = string
        # possible values: indel, snp, unknown

        # gold standard sequence used for comparing against.
        self.standardSequence = None
        # reference to CodeableConcept: CodeableConcept

        # start position of the sequence. if the coordinate system is either
        # 0-based or 1-based, then start position is inclusive.
        self.start = None
        # type = int

        # end position of the sequence.if the coordinate system is 0-based then
        # end is is exclusive and does not include the last position. if the
        # coordinate system is 1-base, then end is inclusive and includes the last
        # position.
        self.end = None
        # type = int

        # the score of an experimentally derived feature such as a p-value
        # ([so:0001685](http://www.sequenceontology.org/browser/current_svn/term/so:0001685)).
        self.score = None
        # reference to Quantity: Quantity

        # which method is used to get sequence quality.
        self.method = None
        # reference to CodeableConcept: CodeableConcept

        # true positives, from the perspective of the truth data, i.e. the number
        # of sites in the truth call set for which there are paths through the
        # query call set that are consistent with all of the alleles at this site,
        # and for which there is an accurate genotype call for the event.
        self.truthTP = None
        # type = int

        # true positives, from the perspective of the query data, i.e. the number
        # of sites in the query call set for which there are paths through the
        # truth call set that are consistent with all of the alleles at this site,
        # and for which there is an accurate genotype call for the event.
        self.queryTP = None
        # type = int

        # false negatives, i.e. the number of sites in the truth call set for
        # which there is no path through the query call set that is consistent
        # with all of the alleles at this site, or sites for which there is an
        # inaccurate genotype call for the event. sites with correct variant but
        # incorrect genotype are counted here.
        self.truthFN = None
        # type = int

        # false positives, i.e. the number of sites in the query call set for
        # which there is no path through the truth call set that is consistent
        # with this site. sites with correct variant but incorrect genotype are
        # counted here.
        self.queryFP = None
        # type = int

        # the number of false positives where the non-ref alleles in the truth and
        # query call sets match (i.e. cases where the truth is 1/1 and the query
        # is 0/1 or similar).
        self.gtFP = None
        # type = int

        # query.tp / (query.tp + query.fp).
        self.precision = None
        # type = int

        # truth.tp / (truth.tp + truth.fn).
        self.recall = None
        # type = int

        # harmonic mean of recall and precision, computed as: 2 * precision *
        # recall / (precision + recall).
        self.fScore = None
        # type = int

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'indel', 'snp', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'indel, snp, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_Quality',
             'child_variable': 'score'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_Quality',
             'child_variable': 'method'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Sequence_Quality',
             'child_variable': 'standardSequence'},
        ]


class Sequence_Repository(fhirbase):
    """Raw data describing a biological sequence.
    """

    def __init__(self, dict_values=None):
        # click and see / restful api / need login to see / restful api with
        # authentication / other ways to see resource.
        self.type = None
        # type = string
        # possible values: directlink, openapi, login, oauth, other

        # uri of an external repository which contains further details about the
        # genetics data.
        self.url = None
        # type = string

        # uri of an external repository which contains further details about the
        # genetics data.
        self.name = None
        # type = string

        # id of the variant in this external repository. the server will
        # understand how to use this id to call for more info about datasets in
        # external repository.
        self.datasetId = None
        # type = string

        # id of the variantset in this external repository. the server will
        # understand how to use this id to call for more info about variantsets in
        # external repository.
        self.variantsetId = None
        # type = string

        # id of the read in this external repository.
        self.readsetId = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'directlink', 'openapi', 'login', 'oauth', 'other']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'directlink, openapi, login, oauth, other'))
