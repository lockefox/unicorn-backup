# unicorn-backup
B2 backup utility for DozingUnicorn

## Use

`unicorn-backup sync [src_dir]`

Will parse folders named `YYYY-MM-DD_*` and upload them into `b2://<bucket_name>/<path_header>/YYYY/<original_folder_name>`

For any failed uploads: `unicorn-backup sync-single [src_dir] --force-upload`
