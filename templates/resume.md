# {{ info.name }} - {{ info.headline }}

{% if info.location %}
- **Location:** {{ info.location }}
{% endif %}
{% if info.phone %}
- **Phone:** {{ info.phone }}
{% endif %}
{% if info.email %}
- **Email:** {{ info.email }}
{% endif %}

## About Me

{{ summary | markdown }}

## Experience

{% for workplace in experience %}
### {{ workplace.title }} · {{ workplace.name }}

**{{ workplace.location }} · {{ workplace.date }}**

{% for subsection in workplace.subsections %}
- {{ subsection.description | markdown }}
{% endfor %}

{% endfor %}

## Education

{% for school in education %}
### {{ school.name }}

**{{ school.date }} · {{ school.degree }}**

{% endfor %}

## Certifications

{% for certification in certifications %}
  * [{{certification.name}}]({{certification.url}}) ({{certification.date}})
{% endfor %}

## Projects

{% for project in projects %}
### [{{ project.name }}]({{ project.url }})

{{ project.description | markdown }}

{% endfor %}

## Skills

{% for skill in skills %}
- {{ skill }}
{% endfor %}

## Interests

{% for interest in interests %}
- {{ interest }}
{% endfor %}

## Contact

{% for item in social %}
- **{{ item.name }}:** [{{ item.display }}]({{ item.url }})
{% endfor %}
