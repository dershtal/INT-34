В hosts.ini указать хост на котором требуется настройка и установка PostgreSQL

Запуск командой в корневой директории проекта

```bash
ansible-playbook -i hosts.ini site.yml --ask-become-pass
```
