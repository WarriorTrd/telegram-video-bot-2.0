# 🔄 Wiki Sync Guide / Руководство по синхронизации Wiki

Это руководство объясняет, как работает автоматическая синхронизация Wiki и как её использовать.

## 🤖 Автоматическая синхронизация

### Как это работает

1. **Триггеры синхронизации:**
   - При push в ветку `main` с изменениями в папке `wiki/`
   - Ручной запуск через GitHub Actions
   - Можно настроить по расписанию

2. **Процесс синхронизации:**
   - GitHub Action клонирует Wiki репозиторий
   - Копирует все `.md` файлы из папки `wiki/`
   - Создает навигацию (`_Sidebar.md`) и футер (`_Footer.md`)
   - Коммитит изменения в Wiki репозиторий

3. **Результат:**
   - Все изменения в `wiki/*.md` автоматически появляются в GitHub Wiki
   - Навигация обновляется автоматически
   - Сохраняется история изменений

## 📝 Редактирование Wiki

### Способ 1: Редактирование файлов (рекомендуется)

```bash
# 1. Отредактируйте файлы в папке wiki/
nano wiki/FAQ.md

# 2. Зафиксируйте изменения
git add wiki/
git commit -m "Update FAQ section"
git push origin main

# 3. Wiki обновится автоматически через 1-2 минуты
```

### Способ 2: Прямое редактирование в GitHub Wiki

1. Перейдите на https://github.com/mirvald-space/Vidzilla/wiki
2. Нажмите "Edit" на любой странице
3. Внесите изменения и сохраните

⚠️ **Внимание:** Изменения, сделанные напрямую в Wiki, будут перезаписаны при следующей автосинхронизации!

### Способ 3: Ручная синхронизация

```bash
# Используйте скрипт для ручной синхронизации
./scripts/sync-wiki.sh
```

## 🛠️ Настройка автосинхронизации

### Активация GitHub Wiki

1. Откройте Settings репозитория
2. Прокрутите до секции "Features"
3. Включите "Wikis"
4. Сохраните изменения

### Настройка прав доступа

GitHub Action использует `GITHUB_TOKEN` с правами:
- `contents: write` - для чтения/записи в репозиторий
- Доступ к Wiki репозиторию

### Ручной запуск синхронизации

1. Перейдите в Actions → "Sync Wiki Documentation"
2. Нажмите "Run workflow"
3. Выберите опции:
   - `force_sync: true` - принудительная синхронизация
4. Нажмите "Run workflow"

## 📊 Мониторинг синхронизации

### Просмотр логов

1. Перейдите в Actions
2. Выберите последний запуск "Sync Wiki Documentation"
3. Просмотрите детальные логи каждого шага

### Статистика синхронизации

В каждом запуске Action создается отчет с:
- Временем синхронизации
- Количеством обновленных страниц
- Размером Wiki
- Статусом выполнения

## 🔧 Кастомизация

### Изменение навигации

Навигация генерируется автоматически в `_Sidebar.md`. Для изменения отредактируйте секцию в `.github/workflows/sync-wiki.yml`:

```yaml
cat > _Sidebar.md << 'EOF'
## 📚 Ваша навигация
* [Страница 1](Page-1)
* [Страница 2](Page-2)
EOF
```

### Изменение футера

Футер генерируется в `_Footer.md`. Настройте его в том же workflow файле.

### Добавление новых страниц

1. Создайте новый `.md` файл в папке `wiki/`
2. Добавьте ссылку в навигацию (опционально)
3. Зафиксируйте изменения - страница появится в Wiki автоматически

## 🚨 Troubleshooting / Решение проблем

### Wiki не обновляется

**Проблема:** Изменения в `wiki/` не появляются в GitHub Wiki

**Решения:**
1. Проверьте, что Wiki включен в настройках репозитория
2. Убедитесь, что изменения были в папке `wiki/`
3. Проверьте логи GitHub Actions
4. Попробуйте ручной запуск workflow

### Ошибка прав доступа

**Проблема:** `Permission denied` при push в Wiki

**Решения:**
1. Убедитесь, что у `GITHUB_TOKEN` есть права на запись
2. Проверьте настройки Actions в Settings → Actions → General
3. Убедитесь, что Wiki репозиторий существует

### Конфликты при синхронизации

**Проблема:** Git конфликты при обновлении Wiki

**Решения:**
1. Не редактируйте Wiki напрямую - используйте файлы в `wiki/`
2. Если нужно сохранить изменения из Wiki, скопируйте их в `wiki/` файлы
3. Принудительная синхронизация перезапишет все изменения

### Отсутствуют файлы в Wiki

**Проблема:** Некоторые страницы не появляются в Wiki

**Решения:**
1. Убедитесь, что файлы имеют расширение `.md`
2. Проверьте, что файлы находятся в корне папки `wiki/`
3. Убедитесь, что файлы не пустые

## 📋 Checklist для настройки

- [ ] ✅ Wiki включен в настройках репозитория
- [ ] ✅ Файлы `.md` созданы в папке `wiki/`
- [ ] ✅ GitHub Action `sync-wiki.yml` добавлен
- [ ] ✅ Права доступа настроены корректно
- [ ] ✅ Первая синхронизация выполнена успешно
- [ ] ✅ Навигация отображается корректно
- [ ] ✅ Все страницы доступны в Wiki

## 🔗 Полезные ссылки

- [GitHub Wiki Documentation](https://docs.github.com/en/communities/documenting-your-project-with-wikis)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Markdown Guide](https://www.markdownguide.org/)

## 📞 Поддержка

Если у вас возникли проблемы с синхронизацией Wiki:

1. Проверьте [GitHub Actions](https://github.com/mirvald-space/Vidzilla/actions)
2. Создайте [Issue](https://github.com/mirvald-space/Vidzilla/issues/new)
3. Обратитесь к администратору проекта

---

*Последнее обновление: $(date +%Y-%m-%d)*