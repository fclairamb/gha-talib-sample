# TA-Lib in GithubActions

This is a quick & dirty sample repo to help you setup [TA-Lib](https://ta-lib.org/), for example if you want to use the python's [ta-lib wrapper](https://mrjbq7.github.io/ta-lib/).

## How
Add the following lines to your github actions file:
```yaml
      - name: Cache talib
        id: cache-talib
        uses: actions/cache@v2
        with:
          path: ta-lib
          key: ${{ runner.os }}-talib
      - name: Build talib
        if: steps.cache-talib.outputs.cache-hit != 'true'
        run: |
          curl http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz -L -o ta-lib-0.4.0-src.tar.gz
          tar -xzf ta-lib-0.4.0-src.tar.gz
          cd ta-lib
          ./configure --prefix=/usr
          make
          sudo make install
      - name: Install talib
        run: |
          cd ta-lib
          sudo make install
```

You can find a complete file [here](https://github.com/fclairamb/gha-talib-sample/blob/main/.github/workflows/tests.yaml).
