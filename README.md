<div align="left" style="position: relative;">
<img src="https://img.icons8.com/?size=512&id=55494&format=png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>AKSIYAMIX.GIT</h1>
<p align="left">
	<em>Empower Your Projects with Aksiyamix!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/Aksiya-Mix-Prod/aksiyamix.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Aksiya-Mix-Prod/aksiyamix.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Aksiya-Mix-Prod/aksiyamix.git?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Aksiya-Mix-Prod/aksiyamix.git?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## 🔗 Quick Links

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Aksiyamix.git is an open-source project solving seamless Docker service orchestration for production and development environments. Key features include managing services like web apps, databases, and workers, automating deployments to Azure VMs, and simplifying Django app configuration. Ideal for developers seeking efficient Docker-based project management and deployment workflows.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Orchestrates Docker services for a production environment, including a web app, PostgreSQL, Redis, Celery worker, and Celery beat. Manages migrations, static files, and runs the web server. Dependencies ensure proper service startup. Configuration is defined in a Docker Compose file.</li><li>Orchestrates Docker services for the project, including web app, PostgreSQL, Redis, Celery worker, and Celery beat. Manages build, container setup, environment variables, ports, volumes, and dependencies. Enables seamless development environment setup and service communication.</li><li>Builds a Docker image for the project by setting up a Python environment, installing dependencies, and copying source code.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>260 Python files</li></ul> |
| 📄 | **Documentation** | <ul><li>Primary language: Python</li><li>File types: yml (3), py (260), example (1), txt (3)</li><li>Containers: Dockerfile</li><li>Install commands using Docker</li><li>Usage commands using Docker</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Automated deployment to an Azure VM upon main branch push</li><li>Utilizes SSH for secure access, updating the application via Git, and managing Docker containers with docker-compose</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Generates Django app configuration files based on directory structure in the apps folder</li><li>Facilitates Django administrative tasks by setting up the environment and executing commands</li></ul> |
| 🧪 | **Testing**       | <ul><li>No test commands provided</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Not specified</li></ul> |
| 🛡️ | **Security**      | <ul><li>Not specified</li></ul> |
| 📦 | **Dependencies**  | <ul><li>github_actions, docker, common.txt, docker-compose.dev.yml, .env.example, python, docker-compose.prod.yml, dockerfile, dev.txt, prod.txt, deploy.yml, python: 3.12-slim</li></ul> |

---

## 📁 Project Structure

```sh
└── aksiyamix.git/
    ├── .github
    │   └── workflows
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── docker-compose.dev.yml
    ├── docker-compose.prod.yml
    ├── requirements
    │   ├── common.txt
    │   ├── dev.txt
    │   └── prod.txt
    └── src
        ├── .env.example
        ├── __init__.py
        ├── apps
        ├── config
        ├── main.py
        └── manage.py
```


### 📂 Project Index
<details open>
	<summary><b><code>AKSIYAMIX.GIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/docker-compose.prod.yml'>docker-compose.prod.yml</a></b></td>
				<td>- Orchestrates Docker services for a production environment, including a web app, PostgreSQL, Redis, Celery worker, and Celery beat<br>- Manages migrations, static files, and runs the web server<br>- Dependencies ensure proper service startup<br>- Configuration is defined in a Docker Compose file.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/docker-compose.dev.yml'>docker-compose.dev.yml</a></b></td>
				<td>- Orchestrates Docker services for the project, including web app, PostgreSQL, Redis, Celery worker, and Celery beat<br>- Manages build, container setup, environment variables, ports, volumes, and dependencies<br>- Enables seamless development environment setup and service communication.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>Builds a Docker image for the project by setting up a Python environment, installing dependencies, and copying source code.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/.github/workflows/deploy.yml'>deploy.yml</a></b></td>
						<td>- Facilitates automated deployment to an Azure VM upon main branch push<br>- Utilizes SSH for secure access, updating the application via Git, and managing Docker containers with docker-compose.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/main.py'>main.py</a></b></td>
				<td>- Generates Django app configuration files based on directory structure in the apps folder<br>- Creates necessary directories and initializes files for models, views, serializers, signals, translations, validators, utils, tasks, admin, tests, and URLs<br>- Configures Django app settings dynamically for each app.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/manage.py'>manage.py</a></b></td>
				<td>Facilitates Django administrative tasks by setting up the environment and executing commands.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/.env.example'>.env.example</a></b></td>
				<td>Define and configure essential environment variables for Django, SMTP, database, Docker, ESKIZ_UZ, Redis, and Payme Payment Settings in the .env.example file.</td>
			</tr>
			</table>
			<details>
				<summary><b>config</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/celery.py'>celery.py</a></b></td>
						<td>- Defines and configures Celery for asynchronous task processing in the Django project<br>- Sets up Celery app, imports Django settings, and auto-discovers tasks<br>- Includes a debug task for testing Celery functionality.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/urls.py'>urls.py</a></b></td>
						<td>- Define the API endpoints for various modules within the Django project, including authentication, user management, tags, services, and more<br>- Integrate Swagger and Redoc for API documentation<br>- Serve media files using Django settings.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/yasg.py'>yasg.py</a></b></td>
						<td>- Generates an API schema view with basic information like title, version, and permissions<br>- This view is publicly accessible and follows the BSD License.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/asgi.py'>asgi.py</a></b></td>
						<td>- Expose the ASGI callable as a module-level variable named 'application' for the config project<br>- Set the DJANGO_SETTINGS_MODULE to 'config.settings' and retrieve the ASGI application for deployment.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/wsgi.py'>wsgi.py</a></b></td>
						<td>- Expose the WSGI callable as a module-level variable named ``application`` for the config project<br>- Set the DJANGO_SETTINGS_MODULE to 'config.settings' and initialize the WSGI application for deployment.</td>
					</tr>
					</table>
					<details>
						<summary><b>settings</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/base.py'>base.py</a></b></td>
								<td>- Defines the foundational settings and configurations for the Django project, including middleware, installed apps, and template settings<br>- Manages key aspects such as security, internationalization, and static file handling<br>- Centralizes essential parameters like time zone, database fields, and media storage paths.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/database.py'>database.py</a></b></td>
								<td>- Configure database and cache settings based on environment variables, supporting both PostgreSQL and SQLite<br>- The file src/config/settings/database.py sets up database connections and cache configurations for the Django project, utilizing environment variables for sensitive information.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/rest_framework.py'>rest_framework.py</a></b></td>
								<td>- Configures default settings for the REST framework, including authentication, rendering, parsing, permissions, pagination, filtering, throttling, versioning, and more<br>- Defines various classes and parameters to ensure consistent behavior and customization across API endpoints.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/languages.py'>languages.py</a></b></td>
								<td>- Defines language settings and paths for internationalization in the Django project<br>- Sets the default language to Uzbek and includes support for Russian<br>- Specifies the locale paths for translations.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/celery.py'>celery.py</a></b></td>
								<td>- Define Celery settings for task scheduling and result backend using Redis<br>- Set timezone to Asia/Tashkent and enable task tracking<br>- Configure a scheduled task to run 'get_currency' daily at midnight.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/sms_providers.py'>sms_providers.py</a></b></td>
								<td>Retrieve and store credentials for Eskiz UZ email and password from environment variables.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/payme.py'>payme.py</a></b></td>
								<td>- Define dynamic Payme payment settings based on environment, loading credentials from environment variables<br>- Set Payme username, password, and callback URL depending on the environment (development or production) to ensure proper configuration for Payme integration within the project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/debug_toolbar.py'>debug_toolbar.py</a></b></td>
								<td>Enables debugging tools for local development by specifying internal IP addresses.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/ckeditor.py'>ckeditor.py</a></b></td>
								<td>- Define custom configurations for CKEditor 5, including toolbar options, block styles, image settings, table properties, and heading options<br>- Customize color palettes for borders and backgrounds, enhancing the editor's visual appearance and functionality<br>- Optimize content creation experience by providing a tailored set of features and styling choices within the CKEditor environment.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/auth.py'>auth.py</a></b></td>
								<td>- Define the authentication settings for the project, specifying the user model and login/logout URLs<br>- This configuration file centralizes authentication-related parameters, ensuring consistency and ease of management across the codebase.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/config/settings/simplejwt.py'>simplejwt.py</a></b></td>
								<td>Define JWT settings for token lifetimes, authentication rules, and serializers in Django project.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>apps</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/main.py'>main.py</a></b></td>
						<td>- Improve application performance by implementing caching mechanisms in the main.py file<br>- This code optimizes data retrieval and processing, enhancing overall system efficiency.</td>
					</tr>
					</table>
					<details>
						<summary><b>features</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for feature functionality in the project, ensuring robustness and reliability.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/apps.py'>apps.py</a></b></td>
								<td>Defines configuration for the 'features' app within the Django project, specifying the default database field type.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the project's features, mapping endpoints to corresponding views<br>- This file plays a crucial role in routing user requests to the appropriate functionality within the codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/admin.py'>admin.py</a></b></td>
								<td>- Improve admin feature functionality by managing user permissions and access control<br>- This code file enhances the project's architecture by centralizing admin-related operations, ensuring secure and efficient management of user roles and permissions.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/models/feature.py'>feature.py</a></b></td>
										<td>- Defines models for features and feature values, ensuring uniqueness based on category and name<br>- Automatically generates slugs and prevents duplicate entries<br>- Supports parent-child relationships between features<br>- Maintains data integrity and consistency within the database.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/views/features.py'>features.py</a></b></td>
										<td>- Defines a view for listing active features with their children, ordered by a specific criteria<br>- It enforces authentication and uses a custom list API view for serialization.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/views/feature_values.py'>feature_values.py</a></b></td>
										<td>Improve user experience by displaying feature values in the application's views.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/serializers/features.py'>features.py</a></b></td>
										<td>- Serializes features with their associated values for the project's frontend display<br>- The code defines the structure and fields to be included when converting Feature model instances into JSON format<br>- This serializer plays a crucial role in ensuring that feature data is properly formatted and accessible for rendering on the user interface.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/features/serializers/feature_values.py'>feature_values.py</a></b></td>
										<td>- Defines serialization for feature values in the project, specifying fields like feature, value, and slug<br>- This serializer is crucial for handling data related to feature values within the codebase architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>wishlists</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/wishlists/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests to ensure the functionality and reliability of the wishlists feature within the project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/wishlists/apps.py'>apps.py</a></b></td>
								<td>Defines configuration for wishlists app in Django project, specifying default auto field and app name.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/wishlists/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for wishlists feature, facilitating navigation within the project<br>- This file plays a crucial role in routing user requests to the appropriate views, enhancing the overall user experience.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/wishlists/admin.py'>admin.py</a></b></td>
								<td>- Manages administrative operations for wishlists in the project, ensuring smooth management and organization of wishlist-related data<br>- This code file plays a crucial role in overseeing and handling administrative tasks related to wishlists within the project architecture.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/wishlists/models/wishlist.py'>wishlist.py</a></b></td>
										<td>- Defines a WishList model that links users to discounts in the project's Django-based architecture<br>- The model inherits from an abstract base model and specifies relationships with user and discount entities<br>- The code ensures data integrity and consistency within the wishlists module.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>branches</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/branches/tests.py'>tests.py</a></b></td>
								<td>- Implements unit tests for the branches functionality in the project, ensuring proper behavior and functionality<br>- This code file plays a crucial role in maintaining the reliability and correctness of the branches feature within the overall codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/branches/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the 'branches' app within the Django project, specifying the default auto field and app name<br>- This file plays a crucial role in organizing and managing the branches functionality within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/branches/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for branch-related operations in a Django project<br>- Maps endpoints to corresponding viewsets for listing, retrieving, creating, updating, and deleting branches<br>- Facilitates routing requests to appropriate handlers, enhancing the project's API functionality and maintainability.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/branches/admin.py'>admin.py</a></b></td>
								<td>Manages administrative tasks for branches in the project, ensuring smooth operations and efficient management.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/branches/models/branch.py'>branch.py</a></b></td>
										<td>- Defines a model for branch companies within the project, including fields for company details, contact information, location, and unique ID generation<br>- The model ensures data integrity and uniqueness by generating a unique ID for each instance<br>- It also provides methods for retrieving the branch address and cleaning data before saving.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/branches/views/branches.py'>branches.py</a></b></td>
										<td>- Manages branch data through CRUD operations, ensuring authentication for each action<br>- Lists all branches, retrieves a specific branch by ID, creates a new branch, partially updates branch details, and deletes a branch<br>- Validates data, returns appropriate responses, and handles errors effectively.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/branches/serializers/branches.py'>branches.py</a></b></td>
										<td>- Defines serializers for BranchCompany model to handle list, detail, creation, and update operations<br>- Serializers include fields like company, title, phone numbers, address, region, district, delivery, longitude, and latitude<br>- Custom logic for creating and validating branch data is implemented.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>ratings</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/ratings/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests to ensure the reliability and accuracy of the ratings functionality within the project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/ratings/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the ratings app within the Django project, specifying the default auto field and app name<br>- This AppConfig class plays a crucial role in managing the ratings functionality within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/ratings/urls.py'>urls.py</a></b></td>
								<td>Defines URL patterns for creating ratings using the RatingCreateViewSet in the Django project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/ratings/admin.py'>admin.py</a></b></td>
								<td>- Enables management of ratings data in the admin interface, facilitating easy access and modification of rating-related information<br>- This functionality enhances the overall user experience by providing a streamlined process for administrators to oversee and update ratings within the system.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/ratings/models/rating.py'>rating.py</a></b></td>
										<td>- Defines a Django model for ratings, linking companies and users with a rating value<br>- Ensures rating value falls within a specific range<br>- Maintains a unique constraint for each company-user pair.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/ratings/views/ratings.py'>ratings.py</a></b></td>
										<td>Defines a view set for creating ratings with authentication permissions, utilizing a custom model view set.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/ratings/serializers/ratings.py'>ratings.py</a></b></td>
										<td>Defines a serializer for ratings data, specifying fields for company and rating value.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>notifications</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/notifications/tests.py'>tests.py</a></b></td>
								<td>Tests the notification functionality to ensure proper functioning within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/notifications/apps.py'>apps.py</a></b></td>
								<td>Defines the configuration for the notifications app within the Django project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/notifications/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the notifications app, facilitating routing and navigation within the project<br>- This file plays a crucial role in directing users to specific functionalities and views within the notifications module, enhancing the overall user experience and interaction with the application.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/notifications/admin.py'>admin.py</a></b></td>
								<td>- Improve notification management in the admin interface by enhancing the functionality for managing notifications<br>- This code file plays a crucial role in the project's architecture by enabling efficient handling and customization of notifications within the admin panel.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/notifications/models/notifications.py'>notifications.py</a></b></td>
										<td>- Defines a model for notifications with various types like News, Follow, and Payment<br>- Includes fields for title, image, and message<br>- Establishes a relationship with the Company model.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>tags</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the tags functionality in the project, ensuring the reliability and accuracy of tag-related features.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/apps.py'>apps.py</a></b></td>
								<td>- Defines configuration for the 'tags' app within the Django project, specifying the default auto field and app name<br>- This file plays a crucial role in organizing and managing the functionality related to tags within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for tag-related functionalities in the Django project, mapping endpoints to corresponding views<br>- The code in this file facilitates routing requests to the appropriate API views for filtering and creating tags within the application.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/admin.py'>admin.py</a></b></td>
								<td>Defines Django admin settings for managing Tag model, displaying key fields and enabling search/filter capabilities.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/create_objects.py'>create_objects.py</a></b></td>
								<td>- Generates tags for the application by creating Tag objects with predefined names and setting them as active<br>- The function bulk creates these Tag objects in the database.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/models/tags.py'>tags.py</a></b></td>
										<td>- Defines a Tag model that inherits from AbstractBaseModel, providing a name field for storing unique tags<br>- The model is structured to interact with the database table 'tag'.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/views/search_tags.py'>search_tags.py</a></b></td>
										<td>- Implements a generic API view for searching tags by name prefix<br>- Returns a list of tag IDs and names based on the provided query parameter.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/views/create_tags.py'>create_tags.py</a></b></td>
										<td>- Enables authenticated users to create tags for discounts using a bulk serializer<br>- The TagsCreateAPIView class handles the POST request to save validated tag data, ensuring a seamless tag creation process within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tags/serializers/create_tags.py'>create_tags.py</a></b></td>
										<td>Handles bulk creation of tags by checking existing tags and creating new ones if needed, then returns the updated list of tags.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>likes</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the likes functionality in the project, ensuring proper behavior and functionality.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/apps.py'>apps.py</a></b></td>
								<td>- Defines configuration for the 'likes' app within the Django project, specifying the default auto field and app name<br>- This code file plays a crucial role in organizing and managing the 'likes' functionality within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for handling discount reactions using Django and REST framework routers<br>- Integrates DiscountReactionViewSet with DefaultRouter to register reactions endpoint<br>- Organizes URLs for easy access and navigation within the likes app.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/admin.py'>admin.py</a></b></td>
								<td>Manages admin functionality for handling likes within the project, contributing to a seamless user experience.</td>
							</tr>
							</table>
							<details>
								<summary><b>signals</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/signals/like_counts.py'>like_counts.py</a></b></td>
										<td>- Handles updating total likes and dislikes for discounts by triggering Celery tasks upon creation or deletion of like/dislike instances<br>- Signals are used to listen for post-save and post-delete events on DiscountLike and DiscountDislike models, respectively<br>- The actual count updates are delegated to a separate task for efficiency.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>tasks</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/tasks/update_discount_likes_count.py'>update_discount_likes_count.py</a></b></td>
										<td>- Implements a Celery task to update likes or dislikes count for a discount in the database using atomic increments/decrements<br>- Handles actions like incrementing likes, decrementing likes, incrementing dislikes, and decrementing dislikes<br>- Retries up to 3 times if the discount is not found.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/models/dislikes.py'>dislikes.py</a></b></td>
										<td>- Defines a model to link users with disliked discounts, ensuring each user can dislike a discount only once and not simultaneously like and dislike the same discount<br>- Tracks which user disliked which discount, enforcing constraints on user and discount choices.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/models/likes.py'>likes.py</a></b></td>
										<td>- Defines a model to link users with liked discounts, ensuring each user can like a discount only once and not simultaneously like and dislike the same discount<br>- Tracks user likes and associated discounts, enforcing constraints for active and approved items.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/views/likes.py'>likes.py</a></b></td>
										<td>- Implements a DiscountReactionViewSet for managing likes and dislikes on discounts, providing functionalities to add/remove likes and dislikes, view statistics, and list user's liked and disliked discounts<br>- Handles actions like liking, disliking, and retrieving statistics on discount reactions.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/serializers/dislikes.py'>dislikes.py</a></b></td>
										<td>Serializes dislike data for discounts in the project, ensuring secure and efficient data handling.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/serializers/stats.py'>stats.py</a></b></td>
										<td>- Calculates and provides statistics on likes, dislikes, and user interactions within the likes feature of the project<br>- The serializer class defines fields for total likes, total dislikes, and user interactions, enhancing the user experience by displaying relevant engagement data.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/serializers/likes.py'>likes.py</a></b></td>
										<td>Serializes DiscountLike model data for user interaction, ensuring only specific fields are exposed.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>permissions</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/likes/permissions/permissions.py'>permissions.py</a></b></td>
										<td>- Defines permissions for admin and users to manage their own Likes/Dislikes<br>- Allows admin users full access and restricts regular users to managing their own actions<br>- Checks ownership for DELETE requests and permits GET requests.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>users</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for user-related functionalities in the project, ensuring robustness and reliability.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the users app within the Django project, specifying the default auto field and app name<br>- This file plays a crucial role in organizing and managing the users-related functionality within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for user-related functionalities like forgot password and profile management in the Django project's users app<br>- The code maps specific URLs to corresponding views for handling password reset, profile retrieval, and updates<br>- This file plays a crucial role in routing user requests to the appropriate API views within the project's architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/admin.py'>admin.py</a></b></td>
								<td>Manages administrative functionalities for user accounts in the project, ensuring smooth operations and efficient user management.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/create_objects.py'>create_objects.py</a></b></td>
								<td>- Generates user objects with predefined phone numbers and names, then bulk creates them in the database using the CustomUser model<br>- This functionality is crucial for efficiently populating the user database with test data.</td>
							</tr>
							</table>
							<details>
								<summary><b>management</b></summary>
								<blockquote>
									<details>
										<summary><b>commands</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/management/commands/create_super_user.py'>create_super_user.py</a></b></td>
												<td>Creates a super user with predefined details in the Django user model.</td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/validators/phone_number.py'>phone_number.py</a></b></td>
										<td>Validates phone numbers to ensure they adhere to the required format within the users module of the project.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/models/users.py'>users.py</a></b></td>
										<td>- Define a fully-featured User model with admin permissions, including fields like username, email, phone number, and more<br>- Implement custom validation for phone numbers and handle user data cleaning<br>- Additionally, provide functionality to send emails to users<br>- This model enhances user management within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/views/profile.py'>profile.py</a></b></td>
										<td>- Enables authenticated users to retrieve and update their profile information<br>- Uses Django's authentication system and REST framework for permissions<br>- Inherits from a custom API view class and utilizes a specific serializer for user profile data<br>- Designed to ensure secure access and seamless interaction with user data within the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/views/forgot_password.py'>forgot_password.py</a></b></td>
										<td>- Manages the process of sending a password reset link to a phone number and setting a new password for a user<br>- Validates the token provided in the request against the cache and handles the password update operation securely<br>- This functionality is crucial for user account security and password recovery within the application.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>utils</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/utils/sms_providers.py'>sms_providers.py</a></b></td>
										<td>- The code in `sms_providers.py` file handles the generation and sending of SMS messages for various user actions like password reset and authentication<br>- It interacts with external APIs to obtain authentication tokens and send SMS messages with dynamic content<br>- This utility class centralizes SMS functionality for user-related operations within the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/utils/managers.py'>managers.py</a></b></td>
										<td>- Manages user creation and authentication by extending Django's built-in UserManager<br>- Handles the creation of regular users and superusers with specific permissions and password hashing<br>- Ensures superusers have the correct staff and superuser flags set.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/serializers/profile.py'>profile.py</a></b></td>
										<td>- Enables serialization for user profile data, including fields like username, email, and phone number<br>- Utilizes Django and REST framework for seamless integration with the project's user model<br>- Provides read-only access to certain fields and custom validation logic for user data.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/users/serializers/forgot_password.py'>forgot_password.py</a></b></td>
										<td>- Implements serializers for handling forgot password and setting a new password for users<br>- Validates user input, checks user existence, and sends reset password links via SMS<br>- Manages password reset tokens and generates JWT tokens for authentication<br>- Includes IP address limit checks for security.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>categories</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/categories/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the categories app to ensure functionality and reliability within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/categories/apps.py'>apps.py</a></b></td>
								<td>- Defines configuration for the 'categories' app within the Django project, specifying the default database field type<br>- This AppConfig class is crucial for managing the app's behavior and settings within the larger project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/categories/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for category-related endpoints using Django and REST framework routers<br>- Maps views to specific HTTP methods for listing categories and retrieving children categories based on parent ID<br>- Integrates with the project's category functionality within the specified app structure.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/categories/admin.py'>admin.py</a></b></td>
								<td>- Defines Django admin settings for managing Category models, specifying displayed fields, filter options, and prepopulated slug field<br>- This code enhances the admin interface functionality, streamlining the process of managing and organizing categories within the project.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/categories/models/category.py'>category.py</a></b></td>
										<td>- Define and enforce validation rules for category models, ensuring proper categorization and hierarchy within the system<br>- Implement checks for category levels and icon presence, along with slug generation and uniqueness validation<br>- Maintain data integrity and consistency for managing categories effectively.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/categories/views/category.py'>category.py</a></b></td>
										<td>- Defines view sets for category data retrieval based on parent-child relationships<br>- Manages listing top-level categories and fetching children categories under a specific parent category<br>- Utilizes custom read-only model view sets for efficient data handling.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/categories/serializers/category.py'>category.py</a></b></td>
										<td>Serializes category data for the project, defining the fields to be included in the output.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>boosts</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/boosts/tests.py'>tests.py</a></b></td>
								<td>Improve Boosts functionality by testing Boosts API endpoints.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/boosts/apps.py'>apps.py</a></b></td>
								<td>Defines BoostsConfig class for Django app configuration in src/apps/boosts/apps.py.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/boosts/urls.py'>urls.py</a></b></td>
								<td>Defines URL patterns for boosting functionality within the project, facilitating navigation and interaction with boost-related features.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/boosts/admin.py'>admin.py</a></b></td>
								<td>Manages administrative functionalities for boosts in the project, contributing to the overall architecture.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/boosts/models/boost_tariff.py'>boost_tariff.py</a></b></td>
										<td>- Defines BoostTariff model with quantity and price fields, inheriting from AbstractBaseModel<br>- This model represents boost tariffs within the boosts application, contributing to the overall data structure and functionality of the project.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/boosts/models/boost_discount.py'>boost_discount.py</a></b></td>
										<td>Defines BoostTariff model with a discount field that establishes a ForeignKey relationship with the Discount model.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/boosts/models/company_boost_tariff.py'>company_boost_tariff.py</a></b></td>
										<td>Defines company-specific boost tariffs for quantity and price, linking them to the respective company.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>authentication</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/tests.py'>tests.py</a></b></td>
								<td>Tests user authentication functionality to ensure secure access and data protection within the project's authentication module.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the authentication app within the Django project, specifying the default auto field and app name<br>- This file plays a crucial role in structuring the authentication functionality within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/urls.py'>urls.py</a></b></td>
								<td>- Defines authentication and registration URL patterns for the Django project, integrating JWT authentication with custom views<br>- The file organizes endpoints for user login, token refresh, sending verification codes, and user registration<br>- It plays a crucial role in managing user authentication and registration flows within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/admin.py'>admin.py</a></b></td>
								<td>Manages administrative functionalities for user authentication within the project architecture, ensuring secure access and user management.</td>
							</tr>
							</table>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/views/register.py'>register.py</a></b></td>
										<td>- Handles user registration, verification, and code sending for phone number verification<br>- Utilizes serializers to validate and process data, returning responses with validated data<br>- Implements custom generic API views for registration, code verification, and code sending functionalities.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>utils</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/utils/services.py'>services.py</a></b></td>
										<td>- Generates JWT tokens for user authentication, utilizing the rest_framework_simplejwt library<br>- The function creates a refresh token and an access token for the user, returning them as a dictionary<br>- This service plays a crucial role in enabling secure user authentication within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>services</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/services/username_type.py'>username_type.py</a></b></td>
										<td>- Define a function to determine if a username is an email or phone number<br>- The function validates the input and returns the type accordingly<br>- This code file plays a crucial role in the authentication service by identifying the type of username provided, ensuring proper handling based on the input type.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/authentication/serializers/register.py'>register.py</a></b></td>
										<td>- Handles user registration, code verification, and token generation<br>- Validates user input, sends registration code, verifies code, and creates a new user with validated data<br>- Utilizes Django models, serializers, and cache for user authentication<br>- Integrates with EskizUz SMS provider for code sending.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>products</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the products application to ensure functionality and reliability within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/apps.py'>apps.py</a></b></td>
								<td>Defines the configuration for the 'products' app within the Django project, specifying the default auto field and app name.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for product-related endpoints using Django's path function, connecting requests to the ProductViewSet for handling<br>- This file plays a crucial role in routing incoming requests to the appropriate view functions within the products app, ensuring seamless navigation and interaction with product-related functionalities.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/admin.py'>admin.py</a></b></td>
								<td>Manages administrative functionalities for products within the project, ensuring smooth operations and efficient management of product-related data.</td>
							</tr>
							</table>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/validators/image_size.py'>image_size.py</a></b></td>
										<td>Validates product image size to ensure it meets specified dimensions within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/models/product.py'>product.py</a></b></td>
										<td>- Defines a Django model for products with fields like company, category, title, and image<br>- Establishes relationships with other models and enforces constraints for data integrity.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/views/product.py'>product.py</a></b></td>
										<td>- Handles CRUD operations for products in the API, ensuring authentication and permission checks<br>- Retrieves, lists, creates, updates, partially updates, and deletes products<br>- Utilizes serializers for data manipulation and custom exceptions for error handling<br>- Maintains data integrity and security throughout product management processes.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/serializers/product.py'>product.py</a></b></td>
										<td>- Handles serialization and validation for products in the project<br>- Manages permissions, enforces product count limits, and ensures only authorized users can create or update products<br>- Integrates with the Django REST framework to streamline product data handling within the system.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>permissions</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/products/permissions/permissions.py'>permissions.py</a></b></td>
										<td>- Enforces permissions for editing products based on user roles<br>- Allows company owners and staff to modify products while restricting access for others.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>general</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/general/tests.py'>tests.py</a></b></td>
								<td>- Improve testing coverage for the general application by adding comprehensive test cases in the tests.py file<br>- This will ensure robustness and reliability of the general application module within the codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/general/apps.py'>apps.py</a></b></td>
								<td>Defines configuration for the 'general' app within the Django project, specifying default database field and app name.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/general/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the general application, mapping specific URLs to corresponding views<br>- This file plays a crucial role in routing user requests to the appropriate functionality within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/general/admin.py'>admin.py</a></b></td>
								<td>Improve data management and access control in the admin interface for the general application.</td>
							</tr>
							</table>
							<details>
								<summary><b>tasks</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/general/tasks/get_currency.py'>get_currency.py</a></b></td>
										<td>- Retrieve and print the latest USD to UZS exchange rate and its establishment date from a specified URL using requests library<br>- This task is executed asynchronously as a shared task using Celery, enhancing the project's scalability and performance.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/general/validators/validators.py'>validators.py</a></b></td>
										<td>Validate user input to ensure data integrity and security within the general application module.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/general/models/general.py'>general.py</a></b></td>
										<td>- Validate and store company balance replenishment limits and currency exchange rates in the database<br>- Ensure the minimum replenishment amount is less than the maximum amount to prevent errors<br>- The models maintain data integrity for financial transactions and currency conversions within the application.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>base</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/tests.py'>tests.py</a></b></td>
								<td>Tests the functionality of the base app in the Django project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/apps.py'>apps.py</a></b></td>
								<td>Defines the configuration for the base app in the Django project, including the default database field and signals.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/signals.py'>signals.py</a></b></td>
								<td>- Handles file deletion operations for objects in the base app by utilizing Django signals<br>- The code in signals.py listens for post_delete and pre_save signals to trigger functions that delete associated files<br>- This ensures that files are cleaned up when objects are deleted or updated within the base app.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/pagination.py'>pagination.py</a></b></td>
								<td>- Implements custom pagination settings for the base application using the PageNumberPagination class from the rest_framework module<br>- Sets default page size, page query parameter, page size query parameter, and maximum page size for the pagination functionality in the project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/authenticate.py'>authenticate.py</a></b></td>
								<td>- Improve user authentication by validating credentials and generating JWT tokens<br>- Ensure active user status and handle exceptions gracefully<br>- This code file enhances security and user experience within the project's authentication flow.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/admin.py'>admin.py</a></b></td>
								<td>Defines a custom admin class in Django to handle model saving with user tracking.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/exceptions.py'>exceptions.py</a></b></td>
								<td>Defines a custom exception class to handle API errors with specified details and codes.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/handlers.py'>handlers.py</a></b></td>
								<td>Handles exceptions related to protected database objects, providing a custom response message.</td>
							</tr>
							</table>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/validators/validators.py'>validators.py</a></b></td>
										<td>- Validates image size and YouTube URLs in the base application, ensuring images meet specified dimensions and YouTube URLs are valid<br>- The code enhances data integrity by preventing invalid image uploads and incorrect YouTube URLs.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/models/base.py'>base.py</a></b></td>
										<td>- Enhances data integrity and consistency by normalizing text fields before saving in the database<br>- Implements a general abstract base model with auto-generated UUID primary key and timestamp fields for tracking creation and updates<br>- Maintains relationships with user models for auditing purposes.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/views/viewsets.py'>viewsets.py</a></b></td>
										<td>- Defines custom viewsets for different types of API endpoints in the project architecture<br>- The code file in src/apps/base/views/viewsets.py extends functionality from the rest_framework module to create custom ViewSets for handling various types of requests, such as basic, generic, model-based, and read-only endpoints.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/views/generics.py'>generics.py</a></b></td>
										<td>Defines custom generic API views for handling various CRUD operations in the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/views/api_views.py'>api_views.py</a></b></td>
										<td>Defines a custom API view class for the base app, contributing to the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>utils</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/utils/region_choices.py'>region_choices.py</a></b></td>
										<td>- The code file `region_choices.py` in the `src/apps/base/utils` directory defines region choices for a Django model, providing a list of regions with corresponding integer values and translated names<br>- This file serves the purpose of centralizing and organizing region choices within the codebase architecture, enabling easy access and consistency in referencing regions throughout the project.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>services</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/services/normalize_text.py'>normalize_text.py</a></b></td>
										<td>- Normalizes text in CharField and TextFields of Django models by removing extra whitespaces<br>- This service function iterates over the fields of a given model object and joins the text fields after splitting them by whitespaces<br>- This ensures consistent formatting and improves data quality within the project's database.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/services/delete_files.py'>delete_files.py</a></b></td>
										<td>- Manages file deletion for objects in the Django project, ensuring files are removed after object deletion or update<br>- It iterates through object fields, deleting associated files from storage if they exist<br>- This functionality helps maintain data integrity and storage efficiency within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/serializers/abstract_serializer.py'>abstract_serializer.py</a></b></td>
										<td>Implements user-based data tracking for create and update operations in serializers, ensuring proper attribution of user actions within the application.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/serializers/model_serializer.py'>model_serializer.py</a></b></td>
										<td>- Defines a custom model serializer by extending the Django Rest Framework's ModelSerializer and an abstract custom serializer mixin<br>- This code file plays a crucial role in serializing model data within the project's architecture, ensuring efficient data handling and transformation for API responses.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/base/serializers/serializer.py'>serializer.py</a></b></td>
										<td>Defines a custom serializer class that extends the functionality of the Django REST framework serializers.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>payments</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/tests.py'>tests.py</a></b></td>
								<td>Tests payment processing functionality to ensure accurate and reliable payment transactions within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/apps.py'>apps.py</a></b></td>
								<td>Defines the configuration for the payments app within the Django project, specifying the default auto field and app name.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for payment-related views using Django and REST framework routers<br>- Registers endpoints for payment processing and initialization<br>- Integrates these views into the project's URL structure.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/admin.py'>admin.py</a></b></td>
								<td>- Manages administrative tasks for payments within the project, ensuring smooth operations and efficient handling of payment-related functionalities<br>- This code file plays a crucial role in overseeing and managing payment processes, contributing to the overall architecture's robustness and effectiveness.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/models/orders.py'>orders.py</a></b></td>
										<td>- Defines an Order model for payment processing, utilizing an 8-character unique ID and linking to the Transaction model<br>- Tracks order details like company, amount, and payment status<br>- Facilitates order and transaction management within the system architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/models/transactions.py'>transactions.py</a></b></td>
										<td>- Manages payment transactions, capturing details like payment system, status, amount, and errors<br>- Associated with orders, it records a comprehensive payment history.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/views/initialization.py'>initialization.py</a></b></td>
										<td>- Implements an API for Payme merchant API Initialization, creating new unpaid orders, generating Payme parameters, and providing frontend data for redirection to Payme's payment page<br>- This code file resides in the 'src/apps/payments/views/initialization.py' path within the project structure.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/views/payments.py'>payments.py</a></b></td>
										<td>- Implements API endpoints for handling payment transactions, including creating, performing, and canceling transactions, as well as checking transaction status and generating transaction history<br>- Facilitates interaction between the app and Payme merchant API, enabling seamless payment processing flow for users.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>utils</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/utils/payme_errors.py'>payme_errors.py</a></b></td>
										<td>- Formats error and success responses from Payme API, providing structured messages and HTTP status codes<br>- The class contains predefined error codes and messages for common scenarios, ensuring consistent response handling across the payments module.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/utils/unique_id.py'>unique_id.py</a></b></td>
										<td>- Generates unique IDs for the Order model in the payments application by creating an 8-character alphanumeric string<br>- This utility function ensures each order has a distinct identifier within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/serializers/orders.py'>orders.py</a></b></td>
										<td>- Serializes Order model data for payments, including company, amount, and payment status<br>- Prevents modification of payment status through read-only fields.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/serializers/transactions.py'>transactions.py</a></b></td>
										<td>Serialize transaction data for payments module.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/serializers/initialization.py'>initialization.py</a></b></td>
										<td>Generates a payment initialization serializer for orders, converting the amount to tiyin and structuring payment data for the merchant.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>permissions</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/permissions/users.py'>users.py</a></b></td>
										<td>- Implement a permission class to restrict user actions based on role<br>- Admins have full access, while regular users can only manage their own payments.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/payments/permissions/payme.py'>payme.py</a></b></td>
										<td>Verifies Payme merchant API authentication using Basic Auth credentials against settings in Django.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>companies</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/tests.py'>tests.py</a></b></td>
								<td>- Improve test coverage for the companies app by adding comprehensive unit tests in the tests.py file<br>- This ensures robustness and reliability in the codebase architecture, enhancing overall project quality and stability.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the 'apps.companies' module within the Django project, specifying the default auto field type<br>- This AppConfig class plays a crucial role in managing the behavior and metadata of the companies app within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for various company-related views, including checking usernames, company operations, timetable management, and ratings<br>- Organizes endpoints for listing, creating, updating, and deleting companies and their timetables, as well as rating companies<br>- Facilitates structured navigation and interaction with company data within the project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/generate_objects.py'>generate_objects.py</a></b></td>
								<td>Generates objects for company entities in the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/admin.py'>admin.py</a></b></td>
								<td>- Registers the Company model with the Django admin interface, allowing administrators to manage company data efficiently<br>- This code file plays a crucial role in the project architecture by enabling seamless interaction with company-related information within the admin panel.</td>
							</tr>
							</table>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/validators/company_logo_size.py'>company_logo_size.py</a></b></td>
										<td>Validates company logo and icon sizes to ensure they meet specified dimensions and file size limits within the project's company module.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/validators/company_banner_size.py'>company_banner_size.py</a></b></td>
										<td>Validates company banner size and dimensions to ensure they meet specified criteria for upload in the project's company application.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/validators/company_video_size.py'>company_video_size.py</a></b></td>
										<td>Validates the size of company videos to ensure they do not exceed 15 MB.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/models/company_time_table.py'>company_time_table.py</a></b></td>
										<td>Generates unique CompanyTimeTable IDs and enforces constraints for company and branch schedules, ensuring start times precede end times.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/models/company.py'>company.py</a></b></td>
										<td>- Defines the data structure and behavior of a Company model within the project, encompassing various attributes such as owner details, contact information, ratings, and geographical data<br>- It also includes methods for generating unique identifiers and cleaning data before saving<br>- This model serves as a core entity for managing company-related information and interactions within the system.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/views/company_time_table.py'>company_time_table.py</a></b></td>
										<td>- Handles CRUD operations for company timetables, including listing, retrieving, creating, updating, and deleting entries<br>- Implements necessary permissions for authenticated users<br>- The code provides endpoints to interact with company time tables, ensuring data integrity and security within the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/views/ratings.py'>ratings.py</a></b></td>
										<td>- Implements functionality to create and update ratings for companies based on user input<br>- Calculates total weighted rating and updates rating counts accordingly<br>- Provides an endpoint for managing company ratings within the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/views/company.py'>company.py</a></b></td>
										<td>- Implements ViewSets for CRUD operations on Company objects, including listing, retrieving, creating, updating, and deleting companies<br>- Utilizes serializers for data manipulation and authentication permissions for secure access control<br>- Supports actions like checking username availability and interacting with company data through RESTful endpoints.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/serializers/company_time_table.py'>company_time_table.py</a></b></td>
										<td>- Manages serialization for company time table data, ensuring proper handling of create, update, and retrieve operations<br>- Maintains consistency in data structure and read-only fields across different serializer actions.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/serializers/ratings.py'>ratings.py</a></b></td>
										<td>Serialize company ratings data for API responses.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/serializers/company.py'>company.py</a></b></td>
										<td>- Enhances company data serialization by providing tailored views for list, creation, update, deletion, and retrieval operations<br>- Optimizes data presentation and manipulation for improved user experience and efficient data management within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>choice</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/choice/disctrict.py'>disctrict.py</a></b></td>
										<td>Define district and region choices for various regions in Uzbekistan.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/choice/country.py'>country.py</a></b></td>
										<td>Define country choices for specific locations in the project's Django application.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>enums</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/companies/enums/week_day.py'>week_day.py</a></b></td>
										<td>Define the order of the week days using integer choices for the companies app.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>discounts</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/tests.py'>tests.py</a></b></td>
								<td>Verifies discount calculation accuracy in the discounts module, ensuring correct application of promotional offers.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/apps.py'>apps.py</a></b></td>
								<td>Defines configuration for discounts app, including signal imports.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the discounts application, facilitating navigation within the project<br>- This file plays a crucial role in routing user requests to the appropriate views, enhancing the overall user experience.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/admin.py'>admin.py</a></b></td>
								<td>- Manages discount administration functionality within the project architecture, ensuring seamless handling of discount-related operations<br>- This code file plays a crucial role in overseeing the configuration and management of discounts, contributing to the overall efficiency and organization of the system.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/choices.py'>choices.py</a></b></td>
								<td>Define integer choices for currency and discount types in the Django application.</td>
							</tr>
							</table>
							<details>
								<summary><b>signals</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/signals/discount_feature.py'>discount_feature.py</a></b></td>
										<td>Updates discount prices based on new features to maintain accurate pricing in the system.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/validators/image_size.py'>image_size.py</a></b></td>
										<td>Validate discount image size to ensure it meets specified dimensions within the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/validators/video_size.py'>video_size.py</a></b></td>
										<td>- Validate video files for discounts based on format, duration, and resolution to ensure compliance with supported extensions, time limits, and quality standards<br>- The code enforces constraints for video files uploaded for discounts, safeguarding against unsupported formats, excessive durations, and inadequate resolutions.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/validators/discount.py'>discount.py</a></b></td>
										<td>Validates various discount types based on specific criteria to ensure data integrity and consistency within the discounts module.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/models/discount_image.py'>discount_image.py</a></b></td>
										<td>- Defines a model for discount images linked to discounts, enforcing image size validation<br>- Automatically updates the associated discount's image when the ordering number is set to 1.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/models/discount_feature.py'>discount_feature.py</a></b></td>
										<td>- Defines a model for discount features with fields like price, quantity, and remainder<br>- Ensures data integrity by validating old price against price and remainder against quantity<br>- Maintains a relationship with discounts and feature values.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/models/discount.py'>discount.py</a></b></td>
										<td>- Defines a Django model for discounts with various attributes like title, price, description, and more<br>- Handles features, validations, and category assignments<br>- Implements methods for feature retrieval, cleaning, and saving discount instances.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>utils</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/utils/unique_id.py'>unique_id.py</a></b></td>
										<td>- Generates unique company IDs by combining random letters and digits<br>- Located in the discounts app, this code file plays a crucial role in assigning distinct identifiers within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/serializers/discount_image.py'>discount_image.py</a></b></td>
										<td>- Serialize discount image data for the discounts app, mapping fields to the DiscountImage model<br>- The DiscountImageSerializer class defines the structure for handling discount image information, including discount, image, ordering number, and creation timestamp<br>- It ensures proper data representation for discount images within the project architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/serializers/discount_feature.py'>discount_feature.py</a></b></td>
										<td>Serializes discount feature data for the project's architecture, focusing on specific fields for DiscountFeature model.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/discounts/serializers/discount.py'>discount.py</a></b></td>
										<td>- Handles serialization and database transactions for creating and updating discount objects<br>- Manages features, images, and validation, ensuring data integrity<br>- Supports atomic operations for maintaining consistency in the discount creation and update processes within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>services</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the services module, ensuring functionality and reliability within the project's codebase architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/apps.py'>apps.py</a></b></td>
								<td>- Defines configuration for the services app within the Django project, specifying the default auto field and app name<br>- This file plays a crucial role in organizing and managing the services module within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for service-related API endpoints in the Django project<br>- Maps specific URLs to corresponding views for listing and creating services.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/admin.py'>admin.py</a></b></td>
								<td>- Defines custom admin settings for the Service model in Django, enhancing the display and editing capabilities within the admin interface<br>- The code in this file centralizes the configuration for how Service instances are presented and managed, ensuring a streamlined user experience for administrators interacting with service data.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/create_objects.py'>create_objects.py</a></b></td>
								<td>- Generates services for the project by creating instances of the Service model with predefined names and settings<br>- The code populates the database with various service options, enhancing the project's functionality and user experience.</td>
							</tr>
							</table>
							<details>
								<summary><b>translations</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/translations/services.py'>services.py</a></b></td>
										<td>Enables translation of service names within the project's services module.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/validators/image_size.py'>image_size.py</a></b></td>
										<td>Validates image size to ensure it meets specified dimensions within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/models/services.py'>services.py</a></b></td>
										<td>- Implements a Django model for services with fields for name, slug, icon, and activation status<br>- Ensures slug uniqueness and icon presence when service is active<br>- Extends AbstractBaseModel and handles custom exceptions.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/views/service_create.py'>service_create.py</a></b></td>
										<td>Enables authenticated users to create new services using a custom API view and serializer within the project's services module.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/views/service_list.py'>service_list.py</a></b></td>
										<td>Implements a custom list API view for services, filtering active services and serializing them using a specific serializer.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/serializers/service_create.py'>service_create.py</a></b></td>
										<td>Enables creation of service objects by defining serialization rules for service data.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/services/serializers/service_list.py'>service_list.py</a></b></td>
										<td>- Serializes service data for display, extracting specific fields like ID, name, and icon<br>- This serializer is crucial for rendering service information in a structured format within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>comments</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the comments functionality in the project, ensuring robustness and reliability.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/apps.py'>apps.py</a></b></td>
								<td>Defines the configuration for the comments app within the Django project, including the default database field and signals.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for comments using Django and REST framework routers, enabling easy endpoint configuration and viewset registration<br>- This file plays a crucial role in structuring the API routes for managing discount comments within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/admin.py'>admin.py</a></b></td>
								<td>Manages administrative tasks for comments in the project, ensuring smooth operations and organization.</td>
							</tr>
							</table>
							<details>
								<summary><b>signals</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/signals/comment_count.py'>comment_count.py</a></b></td>
										<td>- Manages comment count updates for discounts, ensuring accuracy and preventing race conditions in a Django project<br>- Signals trigger Celery tasks to increment or decrement counts based on comment creation, update, or deletion events<br>- This architecture maintains data integrity and scalability by offloading count updates to asynchronous tasks.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>tasks</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/tasks/celery_count_comments.py'>celery_count_comments.py</a></b></td>
										<td>- Implements a Celery task to update comment counts for discounts in the database<br>- Increments or decrements the count based on the specified action ('increment' or 'decrement')<br>- Utilizes F() expressions for atomic database updates.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>paginations</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/paginations/paginations.py'>paginations.py</a></b></td>
										<td>Defines custom pagination settings for comment replies in the project, specifying the page size, query parameters, and maximum page size.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/validators/comment_max_length.py'>comment_max_length.py</a></b></td>
										<td>- Validates comment length to ensure it does not exceed the specified limit<br>- Handles various comment-related validations, enforcing business rules and content restrictions<br>- The class encapsulates methods for validating comments based on length and custom criteria, raising errors if validation rules are violated.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/models/comment.py'>comment.py</a></b></td>
										<td>- Defines a Django model for comments, linking users, discounts, and parent comments<br>- Implements constraints to ensure data integrity and provides a manager for filtering active comments.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/views/comments.py'>comments.py</a></b></td>
										<td>- Manages interactions with discount comments and replies, allowing users to add, list, and delete comments and replies<br>- Utilizes custom pagination and permissions for admin or comment owner actions<br>- Implements efficient database queries using select_related and prefetch_related for optimal performance.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>managers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/managers/comment_manager.py'>comment_manager.py</a></b></td>
										<td>- Implements custom queryset to exclude soft-deleted comments, ensuring only active comments are retrieved<br>- Utilizes soft-deletion to maintain data integrity and preserve comment threads<br>- Enables seamless conversation flow by keeping replies visible even if parent comments are deleted.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/serializers/comments.py'>comments.py</a></b></td>
										<td>- Serializes parent and child comments, including user data, for dynamic handling of custom user models<br>- Provides flexibility and reusability in nested serializers, controlling user data representation<br>- Handles pagination for child comments, ensuring efficient data retrieval and presentation.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>permissions</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/comments/permissions/permissions.py'>permissions.py</a></b></td>
										<td>- Defines permissions for admin and comment owners in the comments app, allowing admin users to perform any action and regular users to manage only their own comments<br>- The code ensures that authenticated users can access the specified HTTP methods based on their role.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>appeals</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/appeals/tests.py'>tests.py</a></b></td>
								<td>Tests the functionality of the appeals application to ensure it meets requirements and functions as expected within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/appeals/apps.py'>apps.py</a></b></td>
								<td>Defines the configuration for the appeals app within the Django project.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/appeals/urls.py'>urls.py</a></b></td>
								<td>Defines URL patterns for creating appeals using the AppealCreateViewSet in the Django project's appeals app.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/appeals/admin.py'>admin.py</a></b></td>
								<td>- Manages administrative operations for appeals within the project, ensuring efficient handling and resolution of appeals-related tasks<br>- This code file plays a crucial role in overseeing and managing the appeals process, contributing to the overall architecture's functionality and effectiveness.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/appeals/models/appeal.py'>appeal.py</a></b></td>
										<td>- Define the Appeal model with user, company, phone number, subject, and message fields<br>- Ensure data integrity by setting constraints on user and company choices<br>- Maintain a clean database structure by utilizing the AbstractBaseModel.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/appeals/views/appeals.py'>appeals.py</a></b></td>
										<td>- Defines a view set for creating appeals, ensuring only authenticated users can access it<br>- Handles appeal creation by associating the user with the request to save the appeal data.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/appeals/serializers/appeals.py'>appeals.py</a></b></td>
										<td>Enhances appeal creation by associating user with request data.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>followers</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/followers/tests.py'>tests.py</a></b></td>
								<td>- Improve testing coverage for the followers feature by enhancing the test suite in the 'followers/tests.py' file<br>- This file plays a crucial role in ensuring the reliability and functionality of the followers module within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/followers/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the 'followers' app within the Django project, specifying the default database field and app name<br>- This code file plays a crucial role in organizing and managing the functionality related to followers within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/followers/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the followers app, facilitating navigation within the project<br>- This file plays a crucial role in routing user requests to the appropriate views, enhancing the overall user experience.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/followers/admin.py'>admin.py</a></b></td>
								<td>Manages administrative tasks for follower data in the project, ensuring smooth operations and efficient management of user interactions.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/followers/models/follower.py'>follower.py</a></b></td>
										<td>- Define a model to manage followers of companies, ensuring users cannot follow the same company multiple times<br>- The model establishes relationships between users and companies, enforcing data integrity and preventing duplicate follow actions.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>complaints</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/complaints/tests.py'>tests.py</a></b></td>
								<td>Improve test coverage for the complaints app by adding comprehensive unit tests.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/complaints/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the complaints app within the Django project, specifying the default auto field and the app's name<br>- This AppConfig class plays a crucial role in managing the complaints app's behavior and settings within the overall project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/complaints/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the complaints app, facilitating navigation within the project<br>- This file plays a crucial role in routing user requests to the appropriate views, ensuring seamless interaction with the complaints functionality.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/complaints/admin.py'>admin.py</a></b></td>
								<td>Manages administrative functionalities for complaints in the project, ensuring smooth handling and resolution of user-reported issues.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/complaints/models/complaint.py'>complaint.py</a></b></td>
										<td>- Defines a model for user complaints, linking users to discounts and companies<br>- Captures complaint details like message, first name, and completion status<br>- Implements constraints to ensure unique user-discount pairs.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>tops</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the 'tops' application to ensure functionality and reliability within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the 'tops' app within the Django project, specifying the default auto field and app name<br>- This AppConfig class plays a crucial role in managing the behavior and metadata of the 'tops' app within the larger project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the 'tops' app, facilitating navigation within the project<br>- This file plays a crucial role in routing user requests to the appropriate views, enhancing the overall user experience.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/admin.py'>admin.py</a></b></td>
								<td>Manages administrative functionalities for the tops application, ensuring smooth operations and user management within the codebase architecture.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/models/top_calendar.py'>top_calendar.py</a></b></td>
										<td>- Define a model representing booked days in a month, storing year, month, and booked days as a boolean grid<br>- Ensure uniqueness by year and month.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/models/top_tariff.py'>top_tariff.py</a></b></td>
										<td>- Defines a model for top tariffs in the project, storing quantity and price information<br>- This model extends an abstract base model and is structured to interact with the database table 'top_tariff'.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/models/top_discount.py'>top_discount.py</a></b></td>
										<td>Defines a model for top discounts in the project, linking discounts to specific dates.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/tops/models/company_top_tariff.py'>company_top_tariff.py</a></b></td>
										<td>- Defines a model for company top tariffs in the Django project, storing quantity and price information<br>- The model is linked to the Company model and enforces constraints on the price field<br>- This file contributes to the project's architecture by managing top tariff data for companies.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>advertisements</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/advertisements/tests.py'>tests.py</a></b></td>
								<td>Implements unit tests for the advertisement functionality to ensure proper behavior and reliability within the project's architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/advertisements/apps.py'>apps.py</a></b></td>
								<td>Defines the configuration for the advertisements app within the Django project, specifying the default auto field and the app name.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/advertisements/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for the advertisements app, facilitating navigation within the project<br>- This file plays a crucial role in routing user requests to the appropriate views, enhancing the overall user experience and ensuring seamless interaction with the advertisements functionality.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/advertisements/generate_objects.py'>generate_objects.py</a></b></td>
								<td>- Generates 10 unique Advertisement objects with random data, ensuring each has a distinct title and image path<br>- Utilizes bulk_create to efficiently save all objects at once.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/advertisements/admin.py'>admin.py</a></b></td>
								<td>Manages administrative functionalities for advertisements in the project, ensuring smooth operations and organization.</td>
							</tr>
							</table>
							<details>
								<summary><b>validators</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/advertisements/validators/validate_image_size.py'>validate_image_size.py</a></b></td>
										<td>Validates image size and dimensions for advertisements to ensure they meet specified criteria.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/advertisements/models/advertisement.py'>advertisement.py</a></b></td>
										<td>- Defines Advertisement model with unique ID generation, URL validation, and date constraints<br>- Ensures each instance has a unique 8-digit ID and validates URL format<br>- Implements date validation to ensure the start date is before the end date<br>- This model represents companies' advertisements within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<details>
						<summary><b>packets</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/tests.py'>tests.py</a></b></td>
								<td>Improve test coverage for packet handling functionality in the project's test suite.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/apps.py'>apps.py</a></b></td>
								<td>- Defines the configuration for the 'packets' app within the Django project, specifying the default database field and app name<br>- This AppConfig class plays a crucial role in managing the behavior and characteristics of the 'packets' app within the larger project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/urls.py'>urls.py</a></b></td>
								<td>- Defines URL patterns for packet-related API endpoints using Django and REST framework routers, enabling easy routing and viewset registration<br>- This file plays a crucial role in structuring the API endpoints for packets within the project architecture.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/admin.py'>admin.py</a></b></td>
								<td>Manages administrative tasks for packet data within the project, ensuring smooth operations and organization.</td>
							</tr>
							</table>
							<details>
								<summary><b>models</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/models/packets.py'>packets.py</a></b></td>
										<td>- Defines a Packet model for payments with quantity and price fields, ensuring data integrity and validation<br>- This model is crucial for managing and storing information related to packages used for posting discounts within the project's architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>views</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/views/packets.py'>packets.py</a></b></td>
										<td>- Implements a PacketGenericViewSet class that handles listing Packet objects with specific permissions and serialization<br>- Includes methods to retrieve and display packets based on creation date.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>serializers</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/serializers/packets.py'>packets.py</a></b></td>
										<td>- Serializes Packet model data with read-only fields for id, quantity, and price<br>- Extends CustomModelSerializer to define serialization behavior.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>permissions</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/src/apps/packets/permissions/permissions.py'>permissions.py</a></b></td>
										<td>- Implement a permission class to restrict access based on user roles<br>- Admins have full access, while company owners can only view packages<br>- The class checks user permissions and company ownership to determine access rights.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- requirements Submodule -->
		<summary><b>requirements</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/requirements/dev.txt'>dev.txt</a></b></td>
				<td>- Facilitates development environment setup by specifying dependencies in dev.txt, referencing common.txt<br>- This file plays a crucial role in managing project dependencies and ensuring a consistent development environment across the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/requirements/prod.txt'>prod.txt</a></b></td>
				<td>Integrate common dependencies for production use in the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/master/requirements/common.txt'>common.txt</a></b></td>
				<td>Manage project dependencies using the provided common.txt file, ensuring compatibility and stability across the codebase architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with aksiyamix.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Container Runtime:** Docker


### ⚙️ Installation

Install aksiyamix.git using one of the following methods:

**Build from source:**

1. Clone the aksiyamix.git repository:
```sh
❯ git clone https://github.com/Aksiya-Mix-Prod/aksiyamix.git
```

2. Navigate to the project directory:
```sh
❯ cd aksiyamix.git
```

3. Install the project dependencies:


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -f docker-compose.dev.yml up --build
```




### 🤖 Usage
Run aksiyamix.git using the following command:
**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
echo 'INSERT-TEST-COMMAND-HERE'

---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Aksiya-Mix-Prod/aksiyamix.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Aksiya-Mix-Prod/aksiyamix.git/issues)**: Submit bugs found or log feature requests for the `aksiyamix.git` project.
- **💡 [Submit Pull Requests](https://github.com/Aksiya-Mix-Prod/aksiyamix.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Aksiya-Mix-Prod/aksiyamix.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Aksiya-Mix-Prod/aksiyamix.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Aksiya-Mix-Prod/aksiyamix.git">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

  #### Name: [Mukhsin Mukhtorov](https://github.com/Mukhsin0508)

- Place: Tashkent, Uzbekistan
- Bio: Backend Developer | ML/AI Enthusiast
- GitHub: [Mukhsin0508](https://github.com/Mukhsin0508)

---
