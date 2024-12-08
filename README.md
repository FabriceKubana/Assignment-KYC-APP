# Telecom KYC System App Project

## Group Members:
- **Fabrice SHEMA KUBANA** - 218004409
- **Liliane Uwera** - 222019122
- **Umutoni Yollanda** - 219002673

## Contributors and Their Contributions

- **Fabrice SHEMA**: Project Implementor
  - Led the implementation of the KYC application, overseeing the overall development process, coding, and ensuring the application met the project goals.

- **Liliane Uwera**: AWS Database Integration
  - Assisted in connecting the KYC system with AWS Relational Database Service (RDS) for secure, scalable, and highly available data storage.
    Ensured smooth database management and high availability.

- **Umutoni Yollanda**: MapReduce Implementation 
  - Demonstrated how MapReduce can be implemented for processing large-scale data. Also worked on integrating the output results into the KYC system’s dashboard,
    enabling real-time display of the results.

- **Team Effort**: 
  - All team members collaborated throughout the project, from design and development to troubleshooting and deployment,
    ensuring successful completion and integration of all components.



## Introduction
 The telecom industry plays a crucial role in enabling communication across regions,
 facilitating economic growth, and connecting people. With the increasing demand
 for secure and regulated telecom services, the need for a robust Know Your Cus
tomer (KYC) system has become critical.

 The KYC process ensures compliance with regulatory requirements by validat
ing customer identities and maintaining a comprehensive record of subscriber de
tails. This system enhances operational efficiency, prevents fraudulent activities,
 and builds trust between the telecom provider and its customers.
 
 To address these needs, project involves developing a Django-based Telecom
 KYC system with KYC App, a web application designed to securely record sub
scriber details during the telecom subscription process. The system is connected
 to an AWS Database to provide reliable and scalable data storage while ensuring
 global accessibility and high performance.

 The project employs a range of tools, libraries, and frameworks to achieve the
 objectives:

- **Backend Framework:** Django (Python)
- **Frontend Technologies:** HTML, CSS, JavaScript (with Bootstrap for re
sponsive design)
  - **Database:** AWS Relational Database Service (RDS) with MySQL for secure
 and scalable data storage
- **Cloud Infrastructure:** Amazon Web Services (AWS) for database hosting, ensuring high availability and reliability
- **Authentication:** Django’s built-in authentication framework with additional role-based access controls for administrators and field agents
- **Development Environment:** Python, Django
- **Version Control:** GitHub for code management and collaboration

### Main Objective

The primary objective of the project is to develop a Telecom KYC System app
 called KYC that records and manages all subscriber details during the telecom
 subscription process, while securely connecting the app to an AWS Database for
 reliable and scalable data storage.

 ### Specific Objectives

 - **Facilitate Customer Registration:** Enable field agents and administrators to register new subscribers efficiently through the KYC app, ensuring accurate data entry.
- **User Roles and Management:** Provide role-based access control, distinguishing between admins and field agents, to streamline responsibilities
- and enhance accountability in the app.
- **Improved Data Accessibility:** Design a centralized AWS-hosted database connected to the KYC app for better data accessibility.
- **Connecting to Hadoop:** Integrate the KYC app with Hadoop for large-scale data storage and processing, allowing for efficient
- handling and analysis of customer data across distributed systems.
- **Integration with Kafka:** Enable real-time data streaming and event processing by integrating Kafka, ensuring fast and reliable communication
- between different components of the system and providing real-time insights into customer activities.

# Technical Implementation: Tools, Libraries, and Frameworks Used

The Telecom KYC System App called KYC is developed using a set of modern
tools, libraries, and frameworks to ensure scalability, security, and efficiency. The
system leverages the flexibility of the Django framework, integrates with a cloud
based AWS database for reliable data storage, and uses a range of technologies
to provide a user-friendly and secure experience for both administrators and field
agents.

## Django Framework 
Django is a high-level Python web framework that simplifies the development of web applications by providing pre-built components
for various functions like authentication, database management, and URL routing. The framework follows the Model-View-Template (MVT) design pattern, 
which is ideal for the KYC system because of its scalability and security features.

- **Authentication System:** Django’s built-in user authentication system makes it easy to manage user roles and access levels (admin, field agents, etc.).
- **Admin Interface:** Django comes with a powerful and customizable admin panel for easy data management and monitoring.

## AWS (Amazon Web Services)

The application is hosted on Amazon Web Services (AWS), which provides reliable
 cloud infrastructure for scalable application deployment and data storage. AWS
 offers:
 - **AWS Relational Database Service (RDS):** Used to manage the MySQL database that stores subscriber data securely.
   RDS ensures that the database is scalable, highly available, and backed up automatically.

- **AWS Identity and Access Management (IAM):** Used to manage access to AWS services securely,
  ensuring that only authorized users can interact with the infrastructure.

  ## MySQL Database Management System (DBMS)

  MySQL is an open-source relational database management system (RDBMS) used
 to manage and store subscriber data securely in the KYC system. MySQL is known
 for its performance, reliability, and ease of use. It provides:

- **Data Integrity:** MySQL ensures that the data is consistent and accurate, which is crucial for the KYC process.

- **ACID Compliance:** MySQL guarantees reliable transaction processing, ensuring that all database operations are completed successfully
  or rolled back in case of failure.

- **Scalability and Performance:** MySQL’s indexing and optimized query processing make it an ideal choice for handling large datasets efficiently,
  ensuring fast data retrieval in the KYC system.

## Django REST Framework (DRF)
 Django REST Framework (DRF) is a powerful toolkit used to build APIs for Django
 applications. In the KYC system, DRF is used to expose specific functionalities of
 the app for integration with other services or third-party applications. Key features:

 - **Serializers:** Used to convert Python objects into JSON format and vice versa, making it easy to handle data exchange between the server and clients.

- **Authentication & Permissions:** DRF provides built-in mechanisms to authenticate users and assign permissions,
  ensuring only authorized users can access the system’s resources.

## Bootstrap (Frontend Framework)

Bootstrap is a front-end framework used to build responsive and mobile-first web
pages. It simplifies the design of the user interface for the KYC system app. Key
benefits:

- **Responsive Design:** Ensures the KYC system is accessible on any device, from desktops to smartphones.

- **Pre-built Components:** Provides pre-designed UI components (buttons, forms, navigation bars) that speed up development
  and ensure a uniform look and feel across the app.

  ## HTML/CSS/JavaScript

These are the core web technologies used to build the user interface of the KYC
system. Together, they enable:

- **HTML:** Defines the structure of the web pages (forms, tables, inputs).

- **CSS:** Styles the web pages, ensuring the app is visually appealing and consistent with the branding.

- **JavaScript:** Adds interactivity and dynamic features to the app, such as real-time validation of subscriber data and interactive forms.

## Git & GitHub (Version Control)

 Git is used for version control, allowing developers to track changes in the codebase,
 collaborate efficiently, and manage releases. GitHub serves as a platform to store
 the code repository, facilitate collaboration, and ensure code quality through pull
 requests and reviews. Benefits include:

 - **Version History:** Keeps track of all changes made to the project, allowing for easy rollback if needed.

- **Collaboration:** Multiple developers can work on the project simultaneously without overwriting each other’s changes.

## Hadoop
Hadoop is an open-source framework for distributed storage and processing of
 large datasets. In KYC system App, Hadoop used to:

- **Big Data Processing:** Handle large volumes of data generated by the KYC system, allowing for efficient data storage and processing across a distributed cluster.
  
- **Scalability:** Provide the capability to scale storage and computation resources as the data grows, ensuring the system can handle increased
  load without performance degradation.

##  Kafka

 Apache Kafka is a distributed event streaming platform used for real-time data
 processing. In KYC system App, Kafka used to:

 - **Real-time Data Streaming:** Capture and stream real-time data events, such as customer registrations, and ensure that the system reacts in real-time.

- **Event-Driven Architecture:** Support the creation of an event-driven architecture, where various components of the system communicate
  through Kafka streams, enabling more responsive and scalable interactions.

# Cloud Service Configurations
   The Telecom KYC System app (KYC) leverages cloud services for various purposes,
 including storing and managing databases. Amazon Web Services (AWS) used to
 configure and manage the infrastructure of the KYC system App especially database.

##  Amazon Relational Database Service (RDS)

RDS used to manage the MySQL database for storing KYC data. The key config
uration settings include:

- **MySQL Database Engine:** The RDS instance is configured to use MySQL as the database engine, optimized for performance and reliability.

- **Multi-AZ Deployment:** RDS is configured for Multi-AZ deployment, where the database is replicated across multiple availability zones
  to ensure high availability and failover support. In the event of an AZ failure, traffic is routed to the standby instance.

- **Automated Backups:** RDS automated backups are enabled, ensuring that data is backed up regularly and can be restored to any point within a retention period.

# Challenges faced and solutions applied.

##  Challenge 1: Integrating the App with Hadoop (MapReduce)

As the KYC system handles large volumes of subscriber data, integrating it with
 Hadoop to leverage MapReduce for distributed data processing was essential. This
 presented challenges in terms of compatibility and efficient data flow between the
 Django-based application and the Hadoop ecosystem.

 A significant challenge arose during the integration of the KYC system with
 Hadoop MapReduce for batch processing of subscriber data. The primary issue was
 related to establishing a stable connection between the Django application and the
 Hadoop cluster. Misconfigurations and dependency issues caused repeated failures
 during integration attempts.

 ###  Solution: Hadoop Configuration

 Correct Hadoop cluster configurations were ensured by reviewing the core-site.xml
 and hdfs-site.xml files for proper settings related to namenode and datanode con
nections. This process included verifying:

## Challenge 2: Integration with Apache Kafka

Real-time data processing with Apache Kafka was introduced to handle the stream
ing of subscriber details and system logs. However, the integration process presented
 several challenges:

 - **Connection Issues:** Establishing a stable connection between the Django-based KYC application and the Kafka cluster was problematic,
   requiring repeated configuration adjustments and troubleshooting.

- **Message Serialization:** Ensuring that messages sent to Kafka were correctly serialized caused compatibility issues.
  Data serialization formats such as JSON and Avro required proper implementation to maintain data integrity.

- **Consumer Group Failures:** During high-load scenarios, consumer groups frequently failed, leading to dropped messages and inconsistent data processing.
  Resolving this required optimizing Kafka’s configuration and consumer logic.

  ###  Solution

  - **Kafka-Python Library:** The Kafka-Python library was used to establish a reliable connection between the KYC application and Kafka producers and consumers.
    This library provided a robust interface for managing message streaming and ensured seamless integration with the Kafka cluster.

- **Message Serialization:** To address serialization challenges, the Avro schema was implemented for serializing and validating messages before sending them to Kafka.
  This approach ensured compatibility across systems and reduced the likelihood of errors during message processing.












 
