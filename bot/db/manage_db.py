import aiosqlite
import asyncio


class DataB:
    def __init__(self):
        loop = asyncio.get_event_loop()
        conn, cur = loop.run_until_complete(self.connect())
        loop.close()
        self.conn, self.cur = conn, cur

    @staticmethod
    async def connect():
        conn = await aiosqlite.connect('ApiKeys.db')
        cur = await conn.cursor()

        await cur.execute('''
            CREATE TABLE IF NOT EXISTS OrgKeys
            (id INT UNIQUE, key TEXT)
        ''')

        await conn.commit()
        return conn, cur

    async def close(self):
        await self.cur.close()
        await self.conn.close()

    async def _update_key(self, id, key):
        await self.cur.execute('''
            INSERT OR REPLACE INTO OrgKeys (id, key)
            VALUES ('%s', '%s')
        ''' % (id, key))
        await self.conn.commit()

    async def _take_key(self, id):
        await self.cur.execute('''
            SELECT key from OrgKeys WHERE id='%s'
        ''' % (id))
        return await self.cur.fetchone()

    async def change_key(self, id, key):
        await self._update_key(id, key)
        return True

    async def get_key(self, id):
        key = await self._take_key(id)
        return key[0]
