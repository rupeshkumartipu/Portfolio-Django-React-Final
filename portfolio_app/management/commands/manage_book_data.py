from django.core.management.base import BaseCommand
from portfolio_app.models import Book
from datetime import datetime

class Command(BaseCommand):
    help = 'Inserts initial data into the Book table and removes duplicates'

    def handle(self, *args, **kwargs):
        # Insert data
        book_data = [
            {
                'title': 'Predictive Modeling in Civil Engineering: An Introduction',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47289-5',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/ab1d81af71e31d441c1f5d7922f7533993515117'
            },
            {
                'title': 'Data-driven Approaches in Civil Engineering Predictions',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47309-0',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/6f9d4df04df950c4122c38df7eb2d8105eeca232'
            },
            {
                'title': 'Python Essentials: A Compact Guide for Practitioners',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47345-8',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/4eb594ccd5bf718a26f1fbca953d01eef571b6fd'
            },
            {
                'title': 'Scikit-Learn Mastery: Hands-On Machine Learning',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47348-9',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/4985e98f74b11f1c7b136c1b01e6869f42a23a02'
            },
            {
                'title': 'TensorFlow Workshop: Deep Learning in Action',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47349-6',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/97e42ea056e010011e2d4b263dc046e7270d6ece'
            },
            {
                'title': 'Web Development Simplified: Django Essentials',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47350-2',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/14b1c77671497756417e089df52b3a30694a63bb'
            },
            {
                'title': 'Web Design Essentials:Crafting Beautiful Experiences with HTML, CSS, & JavaScript',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47408-0',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/8b4d682195be8c5f13410d143b6fefb50491f3ad'
            },
            {
                'title': 'Efficient Coding with Python: Mastering Optimization Techniques',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47409-7',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/bd23770dd3ff296fe64c90e3634dd1af51d7f57b'
            },
            {
                'title': 'Full-Stack Foundations: Django and JavaScript Integration',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47410-3',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/0b55deafef94e84db8a5f16dd573fb547971e308'
            },
            {
                'title': 'Python and NLP: Building Intelligent Applications',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47466-0',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/89a3eeeac85dbbf3e22cd0282f9e5ed214a64c3e'
            },
            {
                'title': 'The Art of Lightweight Programming: Streamlined Web Development',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47467-7',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/7463309c77f380697e151eaf3ec2e6a0cd9d2d4b'
            },
            {
                'title': 'Practical Python AI: From Basics to Advanced NLP Techniques',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47468-4',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/66c601cf3f4184710621757449d340bda0141663'
            },
            {
                'title': 'Python at the Core: Machine Learning & Beyond',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47469-1',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/449faa74dfa151338772ea9d61e7b2dfe8e78cba'
            },
            {
                'title': 'Optimizing Neural Networks with Python',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47470-7',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/eff92607daaee5804ce6115718d1643fa99864d6'
            },
            {
                'title': 'Intelligent Web Development: Merging NLP & Machine Learning',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47473-8',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/039cae320b395c8f86688765d224a0a8ff031116'
            },
            {
                'title': 'C++ Mastery: Unleashing the Power of Modern Programming',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47538-4',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/5454c3bcb89b75a1c85ced55f6df975f99ad0664'
            },
            {
                'title': 'JavaScript Essentials: From Basics to ES6 and Beyond',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47541-4',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/1a6e4dc9f2afa4514d3061f48654fb1fcd286d1c'
            },
            {
                'title': 'Elegant HTML: Crafting Structured Web Content',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47542-1',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/65bf249f7664ca5d1c7aed7c7392d4b0e41aa1b2'
            },
            {
                'title': 'CSS Artistry: A Visual Guide to Innovative Design',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47543-8',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/102c5df90954e421085a2527044214014b9569cc'
            },
            {
                'title': 'The Android Architect: Building Cutting-Edge Apps',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47544-5',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/f570555b2d412b0ba2e0c3b613f70f0f8446056b'
            },
            {
                'title': 'C++ Concurrency in Action: Real-World Multithreading',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47545-2',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/72bea33e2197a63929b6d7455dae3943edee6fa4'
            },
            {
                'title': 'JavaScript Frameworks Explored: Angular, React, and Vue',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47592-6',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/57f1ca15802bf35e5a5d331b8ce5e0640abe6d6b'
            },
            {
                'title': 'Responsive Web Design with HTML5 and CSS3',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47593-3',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/d6cd09e78d058054102823cdc5fc33ff170eef6e'
            },
            {
                'title': 'Advanced Android Patterns: Optimizing Apps for Performance',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47594-0',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/9a8ae27b0b57f47f81f16a6de2376297aaf57863'
            },
            {
                'title': 'The Essence of C++: A Deep Dive into Object-Oriented Programming',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47595-7',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/f475bf4b3c362444863f12227dbda0547d98be7d'
            },
            {
                'title': 'Large Language Models Unveiled: Development and Deployment Strategies',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47597-1',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/d4ee643f87b1539c5a9ce7bcdfffbf13cb7f9260'
            },
            {
                'title': 'Node.js In-Depth: Building Scalable Web Applications',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47599-5',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/f8c8ea2eb0aa4c1f94115499725e96a0c5f147ec'
            },
            {
                'title': 'React.js Essentials: A Modern Front-End Developer\'s Guide',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47603-9',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/ec4977e203b58daea64820dd5670f89a1ae0d193'
            },
            {
                'title': 'Full-Stack JavaScript Development: Mastering Node.js and React.js',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47607-7',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/ff00f83a088228a9d436be910c28aed4704ea475'
            },
            {
                'title': 'Advanced Patterns in Node.js and React.js: Crafting Enterprise-Level Applications',
                'publisher': 'Lambert Academic Publishing',
                'publication_date': '2024-01-01',
                'summary': '',
                'isbn_issn': '978-620-7-47636-7',
                'link': 'https://www.morebooks.shop/shop-ui/shop/book-launch-offer/4b8818fa3a8b66a4975a3e1d7b6d307157bf84e4'
            }
        ]

        for data in book_data:
            Book.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully inserted book data'))

        # Remove duplicates
        unique_entries = set()
        duplicates = []

        for book in Book.objects.all():
            identifier = (
                book.title,
                book.publisher,
                book.publication_date,
                book.isbn_issn,
                book.link
            )
            if identifier in unique_entries:
                duplicates.append(book.id)
            else:
                unique_entries.add(identifier)

        if duplicates:
            Book.objects.filter(id__in=duplicates).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {len(duplicates)} duplicate entries'))
        else:
            self.stdout.write(self.style.SUCCESS('No duplicate entries found'))
