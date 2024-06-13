from django.core.management.base import BaseCommand
from portfolio_app.models import Publication

class Command(BaseCommand):
    help = 'Inserts initial data into the Publication table and removes duplicates'

    def handle(self, *args, **kwargs):
        # Insert data
        publication_data = [
            {
                'sr_no': 1,
                'authors': 'Tipu, Rupesh Kumar; Panchal, VR; Pandya, KS',
                'publication_type': 'Research Article',
                'title': 'An ensemble approach to improve BPNN model precision for predicting compressive strength of high-performance concrete',
                'journal': 'Structures',

                'year': 2022,
                'publisher': 'Elsevier',
                'indexing': 'SCIE (Q2), Scopus',
                'impact_factor': 4.1,
                'doi': ''
            },

            {
                'sr_no': 3,
                'authors': 'Tipu, Rupesh Kumar; Suman; Batra, Vandna',
                'publication_type': 'Research Article',
                'title': 'Development of a hybrid stacked machine learning model for predicting compressive strength of high-performance concrete',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2023,
                'publisher': 'Springer International Publishing Cham',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 4,
                'authors': 'Tipu, Rupesh Kumar; Panchal, VR; Pandya, KS',
                'publication_type': 'Research Article',
                'title': 'Multi-objective optimized high-strength concrete mix design using a hybrid machine learning and metaheuristic algorithm',

                'year': 2023,
                'publisher': 'Springer',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 5,
                'authors': 'Tipu, Rupesh Kumar; Suman; Batra, Vandna',
                'publication_type': 'Research Article',
                'title': 'Enhancing prediction accuracy of workability and compressive strength of high-performance concrete through extended dataset and improved machine learning models',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer International Publishing Cham',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 6,
                'authors': 'Tipu, Rupesh Kumar; Panchal, VR; Pandya, KS',
                'publication_type': 'Research Article',
                'title': 'Enhancing chloride concentration prediction in marine concrete using conjugate gradient-optimized backpropagation neural network',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer International Publishing Cham',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 7,
                'authors': 'Tipu, Rupesh Kumar; Batra, Vandna; Suman; Panchal, VR; Pandya, KS',
                'publication_type': 'Research Article',
                'title': 'Predictive modelling of surface chloride concentration in marine concrete structures: a comparative analysis of machine learning approaches',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer International Publishing Cham',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 8,
                'authors': 'Tipu, Rupesh Kumar; Batra, Vandna; Pandya, KS; Panchal, VR',
                'publication_type': 'Research Article',
                'title': 'Shear capacity prediction for FRCM-strengthened RC beams using Hybrid ReLU-Activated BPNN model',
                'journal': 'Structures',

                'year': 2023,
                'publisher': 'Elsevier',
                'indexing': 'SCIE (Q2), Scopus',
                'impact_factor': 4.1,
                'doi': ''
            },
            {
                'sr_no': 9,
                'authors': 'Kumar, Rahul; Rathore, Ayush; Singh, Rajwinder; Mir, Ajaz Ahmad; Tipu, Rupesh Kumar; Patel, Mahesh',
                'publication_type': 'Research Article',
                'title': 'Prognosis of flow of fly ash and blast furnace slag-based concrete: leveraging advanced machine learning algorithms',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2023,
                'publisher': 'Springer International Publishing Cham',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 10,
                'authors': 'Tipu, Rupesh Kumar; Batra, Vandna; Pandya, KS; Panchal, VR',
                'publication_type': 'Research Article',
                'title': 'Efficient compressive strength prediction of concrete incorporating recycled coarse aggregate using Newton’s boosted backpropagation neural network (NB-BPNN)',
                'journal': 'Structures',

                'year': 2023,
                'publisher': 'Elsevier',
                'indexing': 'SCIE (Q2), Scopus',
                'impact_factor': 4.1,
                'doi': ''
            },
            {
                'sr_no': 11,
                'authors': 'Tipu, Rupesh Kumar; Batra, Vandna; Pandya, KS; Panchal, VR',
                'publication_type': 'Research Article',
                'title': 'Enhancing load capacity prediction of column using eReLU-activated BPNN model',
                'journal': 'Structures',

                'year': 2023,
                'publisher': 'Elsevier',
                'indexing': 'SCIE (Q2), Scopus',
                'impact_factor': 4.1,
                'doi': ''
            },
            {
                'sr_no': 12,
                'authors': 'Tipu, Rupesh Kumar; Arora, Rishabh; Kumar, Kaushal',
                'publication_type': 'Research Article',
                'title': 'Machine learning-based prediction of concrete strength properties with coconut shell as partial aggregate replacement: A sustainable approach in construction engineering',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer International Publishing Cham',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 13,
                'authors': 'Tipu, Rupesh Kumar; Panchal, VR; Pandya, KS',
                'publication_type': 'Research Article',
                'title': 'Machine learning-based prediction of concrete strengths with coconut shell as partial coarse aggregate replacement: a comprehensive analysis and sensitivity study',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 14,
                'authors': 'Kumar, Kaushal; Arora, Rishabh; Tipu, Rupesh Kumar; Dixit, Saurav; Vatin, Nikolai; Arya, Sandeep',
                'publication_type': 'Research Article',
                'title': 'Influence of machine learning approaches for partial replacement of cement content through waste in construction sector',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 15,
                'authors': 'Tipu, Rupesh Kumar; Batra, Vandna; Suman',
                'publication_type': 'Research Article',
                'title': 'Predictive modeling of shear strength in fiber-reinforced cementitious matrix-strengthened RC beams using machine learning',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer International Publishing Cham',
                'indexing': 'Scopus (Q3)',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 16,
                'authors': 'Tipu, Rupesh Kumar; Panchal, VR; Pandya, KS',
                'publication_type': 'Conference',
                'title': 'Prediction of concrete properties using machine learning algorithm',
                'journal': 'Journal of physics: conference series',

                'year': 2022,
                'publisher': 'IOP Publishing',
                'indexing': 'Scopus',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 17,
                'authors': 'Agarwal, Rupanshi; Pathak, Paresh; Tipu, Rupesh Kumar; Singh, Digvijay; Kalnawat, Aarti; Dhabliya, Dharmesh',
                'publication_type': 'Conference',
                'title': 'ANN-Based Scalable Video Encoding Method for Crime Surveillance-Intelligence of Things Applications',
                'journal': '2023 International Conference on Data Science and Network Security (ICDSNS)',

                'year': 2023,
                'publisher': 'IEEE',
                'indexing': 'Scopus, WoS',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 18,
                'authors': 'Arora, Rishabh; Kumar, Kaushal; Dixit, Saurav; Tipu, Rupesh Kumar; Kaul, Padmini; Chauhan, Swati; Raju, Y Kamala; Nijhawan, Ginni; Haindavi, P',
                'publication_type': 'Conference',
                'title': 'Parametric investigation of coconut shells as partial replacement of coarse aggregates in sustainable concrete',
                'journal': 'E3S Web of Conferences',

                'year': 2023,
                'publisher': 'EDP Sciences',
                'indexing': 'Scopus',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 19,
                'authors': 'Tipu, Rupesh Kumar; Panchal, VR; Pandya, KS',
                'publication_type': 'Book Chapter',
                'title': 'Multi-objective optimization of the concrete mixture blended with mineral admixture using machine learning and NSGA-II algorithms',
                'journal': 'Advanced Engineering Optimization Through Intelligent Techniques: Select Proceedings of AEOTIT 2022',

                'year': 2023,
                'publisher': 'Springer Nature Singapore',
                'indexing': 'Scopus',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 20,
                'authors': 'Raghav, Yogita Yashveer; Tipu, Rupesh Kumar; Bhakhar, Ruchika; Gupta, Tanu; Sharma, Kriti',
                'publication_type': 'Book Chapter',
                'title': 'The Future of Digital Marketing: Leveraging Artificial Intelligence for Competitive Strategies and Tactics',
                'journal': 'The Use of Artificial Intelligence in Digital Marketing: Competitive Strategies and Tactics',

                'year': 2024,
                'publisher': 'IGI Global',
                'indexing': 'NA',
                'impact_factor': 0.0,
                'doi': ''
            },
            {
                'sr_no': 21,
                'authors': 'Tipu, R.K., Batra, V., Suman et al.',
                'publication_type': 'Research Article',
                'title': 'Optimizing compressive strength in sustainable concrete: a machine learning approach with iron waste integration',
                'journal': 'Asian Journal of Civil Engineering',

                'year': 2024,
                'publisher': 'Springer Nature',
                'indexing': 'Scopus',
                'impact_factor': 0.0,
                'doi': 'https://doi.org/10.1007/s42107-024-01061-5'
            }
        ]

        for data in publication_data:
            Publication.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted publication data'))

        # Remove duplicates
        unique_entries = set()
        duplicates = []

        for publication in Publication.objects.all():
            identifier = (
                publication.authors,
                publication.publication_type,
                publication.title,
                publication.journal,

                publication.year,
                publication.publisher,
                publication.indexing,
                publication.impact_factor,
                publication.doi
            )
            if identifier in unique_entries:
                duplicates.append(publication.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            Publication.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
