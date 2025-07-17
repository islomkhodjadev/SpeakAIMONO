


1.env must be only in root folder
2. 
For powershell, to get data for db container
```bash
Get-Content ./archive/populate_mock_data_fixed.sql | docker exec -i speakoai-db psql -U postgres -d miniapp
```
3. Dont add bullshit files anywhere except front