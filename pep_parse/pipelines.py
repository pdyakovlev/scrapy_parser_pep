import csv
import datetime as dt
from collections import defaultdict
from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_status_count = defaultdict(int)
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        if item.get('status'):
            self.pep_status_count[
                item['status']] = self.pep_status_count.get(
                item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        results = [('Cтатус', 'Количество')]
        results.extend(self.pep_status_count.items())
        results.append(('Total: ', sum(self.pep_status_count.values())))

        file_format = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{file_format}.csv'
        file_path = BASE_DIR / 'results' / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(results)
