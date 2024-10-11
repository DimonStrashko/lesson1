import re
import codecs
import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Відкриваємо файл для читання
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()

    # Видаляємо html-теги
    clean_text = re.sub(r'<.*?>', '', html_content)

    # Видаляємо порожні рядки або ті, що складаються лише з пробілів
    clean_lines = [line.strip() for line in clean_text.splitlines() if line.strip()]

    # Записуємо очищений текст у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as result:
        result.write("\n".join(clean_lines))

# Виклик функції
delete_html_tags('C:/Users/user/Downloads/draft.html')
